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
        
def success_path(request):
    return HttpResponse("Success")

def update_task(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.title = new_title
    task.description = new_description

    if request.method == 'POST':
        new_title = request.POST.get("new_title")
        new_description = request.POST.get("new_description")

        if new_title and new_description:
            task = Tasks(new_title=new_title, new_description=new_description)
            task.save()
            return HttpResponse("Task updated successfully.")
        else:
            return HttpResponse("All fields must be filled.")
        

def delete_task(request, task_id):
    if request.method == 'POST':
        try:
            task = Tasks.objects.get(pk=task_id)

            task.delete()
            return HttpResponse("Task deleted successfully.")
        except Tasks.DoesNotExist:
            return HttpResponse("Task does not exist!")
