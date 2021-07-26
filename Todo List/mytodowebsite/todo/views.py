from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import Todoform
from .models import Todo
# Create your views here.

def index(request):
    mytodo = Todo.objects.order_by('id')
    form = Todoform()
    context = {'mytodo': mytodo, 'form': form }
    return render(request,'todo/index.html', context)

@require_POST
def addNewTodo(request):
    form = Todoform(request.POST)
    if form.is_valid():
        my_new_todo= Todo(todotext= request.POST['text'])
        my_new_todo.save()
    return redirect('index')

def completeTodo(request,todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('index')

def deleteTodo(request):
    Todo.objects.filter(complete__exact = True).delete()
    return redirect('index')
