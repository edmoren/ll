from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(requests):
    """The home page for Learning Logs."""
    return render(requests, 'learning_logs/index.html')

def topics(requests):
    """Show all Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(requests, 'learning_logs/topics.html', context)

def topic(requests, topic_id):
    """Show a single topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(requests, 'learning_logs/topic.html', context)
