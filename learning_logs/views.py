from django.shortcuts import render

# Create your views here.
def index(requests):
    """The home page for Learning Logs."""
    return render(requests, 'learning_logs/index.html')
