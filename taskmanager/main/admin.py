from django.contrib import admin
from . models import Task # с файла models импортируем клас Task

admin.site.register(Task)   #обращяемся к панели админа на сайте регистируем таблцу Task
# после этого таблица отобржаеся в панели адинистратора

