from django.shortcuts import redirect, render
from app.models import TodoList

def home(request):
    
    tasks = TodoList.objects.all()

    if request.method == 'POST':
        new_task = request.POST.get('new_task')
        priority = request.POST.get('priority')
        task = TodoList(task_name=new_task, priority=priority)
        print(task)
        task.save()

    context = {'tasks': tasks}

    return render(request, 'index.html', context)

def delete(request, pk):

    task = TodoList.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'task_name': task.task_name}
    return render(request, 'delete.html', context)