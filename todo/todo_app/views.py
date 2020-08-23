from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect
from django.utils import timezone
# Create your views here.
def index(request):
    #The hiphen befor date_added will take us to latest to oldest date and (\date_added) this will take oldest to latest
    todo_items=Todo.objects.all().order_by('-date_added')
    return render(request,'todo_app/index.html',{'todo_items':todo_items})

def add_todo(request):
    text=request.POST.get('text')
    date_added=timezone.now()
    todo=Todo(date_added=date_added,text=text)
    todo.save()
    return HttpResponseRedirect('/')

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')