from .models import Task         # ммпортируем ранее созданую рабочуюмодель
from django.forms import ModelForm, TextInput, Textarea       #импорируем инструменты и библиотеки django

class TaskForm(ModelForm):  #имя класа формы принято присваивать как имя Модели+Form
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите название'
            }),

             'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите описание'
            }),


        }
