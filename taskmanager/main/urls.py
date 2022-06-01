from django.urls import path
from . import views
#  импортируем с текущей директории файл views

urlpatterns = [
    path('', views.index, name='home'),     # '' - отслеживаем переход  на главную страницу
    # также обращаемся к  файлу views и вызываем из него функцию index
    path('about', views.about, name='about'),  #  отслеживаем переход на url 'about-us', вызываем функцию about
    path('create', views.create, name='create'),
]
