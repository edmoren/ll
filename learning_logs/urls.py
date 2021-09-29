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
    path('topics/<int:topic_id>/', views.topic, name='topics')
]
