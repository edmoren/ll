from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# utility functions
def check_topic_owner(topic, user):
    if topic.owner != user:
        raise Http404

# Create your views here.
def index(requests):
    """The home page for Learning Logs."""
    return render(requests, 'learning_logs/index.html')

@login_required
def topics(requests):
    """Show all Topics"""
    topics = Topic.objects.filter(owner=requests.user).order_by('date_added')
    context = {'topics': topics}
    return render(requests, 'learning_logs/topics.html', context)

@login_required
def topic(requests, topic_id):
    """Show a single topic"""
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(topic, requests.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(requests, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request.user)

    if request.method != 'POST':
        # No data submitted, return blank
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display blan form for invalid request
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic, request.user)

    if request.method != 'POST':
        # Inital request, prefil form with current entry
        form = EntryForm(instance=entry)
    else:
        # Post data submitted, process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
