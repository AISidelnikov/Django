from django.shortcuts import render, redirect
from main.forms import TaskForm 
from .models import Task
from django.http import HttpResponse

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Index', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = 'Форма была не верной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)

def replace(request):
    task = Task.objects.get(id = request.GET.get('id'))
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            error = 'Форма была не верной'
    form = TaskForm(instance=task)
    context = {
        'form': form,
        'error': error,
        'task': task,
    }
    return render(request, 'main/replace.html', context)

def delete(request):
    try:
        task = Task.objects.get(id=request.POST.get('id'))
        task.delete()
        return redirect('home')
    except:
        return HttpResponse('<h6>Не удаляется</h6>')