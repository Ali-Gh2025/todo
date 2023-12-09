from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import CreateTodoForms, UpdateTodoForms


def hello(request):
    x = Todo.objects.all()
    return render(request, 'hello.html', {'all': x})

# def goodbye(request):
#     return render(request, 'goodbye.html')

def detail(request,todo_id):
    x = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'x': x})

def delete(request,todo_id):
    
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'Todo deleted successfully!','success') #extra tag
    return redirect('hello')


def create(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            # کل داده هامون میرن توی یه دیکشنری به نام کلین دیتا
            Todo.objects.create(title = cd['title'], body = cd['body'] , created = cd['created'])
            messages.success(request, 'Todo Created Successfully', 'success')
            # کلیدهامون رو از کجا گرفتیم؟ از فرمز دات پای که بهش اونجا یه جوری اسم دادیم که همنام باشن که راحت باشیم 
            return redirect('hello')
    else:
        form = CreateTodoForm()
    return render(request, 'create.html', {'form' : form})
    

def update(request, todo_id):
    
    my_todo = Todo.objects.get(id=todo_id)
    
    if request.method == 'POST':
        form = UpdateTodoForms(request.POST, instance=my_todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo created successfully", 'success')
            return redirect('detail', todo_id)
    else: 
        form = UpdateTodoForms(instance=my_todo)
    return render(request, 'update.html', {'form' : form }) 