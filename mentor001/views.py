from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def index(request): 
    # this is your new view
    return render(request, 'index.html')