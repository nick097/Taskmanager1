from django.shortcuts import render, redirect
from . models import Task  # импорруем с текущей дирректории из файла models класс Task
from . forms import TaskForm

def index(request):  # создаем функцию index и передаем параметр request
    tasks = Task.objects.all()  #создаем переменную которая обращается к класу Task и получает все обекты
    return render(request, 'main/index.html', {'title': 'Главная страница сaйта', 'tasks': tasks}) # указываем адрес находясь в папке templates
# используя ключ 'title' передаем в шаблон текст, используя   'tasks' -  передаем все задачи


def about(request):  # создаем функцию about для странички about-us
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)   # создаем переменную в которую записываем новосозданный объект с введенными даными из формы. ПЕРЕДАЕМ ДАННЫЕ методом POST
        if form.is_valid():  # ЕСЛИ ДАННЫЕ КОРРЕКТНЫЕ
            form.save()   # СОХРАНЯЕМ ИХ В БАЗУ ДАННЫХ
            return redirect('home')  # после сохранения данных перенаправляем пользователя на страницу 'home'
        else:
            error = "форма была заполнена неверно"  # если данные введены некоректно выводим ошибку
    form = TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)