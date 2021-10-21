"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Topics page to show all topics.
    path('topics/', views.topics, name='topics'),
    # View and individual topic.
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Add a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    # Add a new entry for a topic.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
