from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Tasks
from django.urls import reverse


# Create your views here.
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        createdAt = request.POST.get("createdAt")
        
        if title and description and createdAt:
            task = Tasks(title=title, description=description, createdAt=createdAt)
            task.save()
            return HttpResponseRedirect(reverse("success_page"))
        else:
            return HttpResponse("All fields are required.")