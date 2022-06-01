from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')) # '' - отслеживаем переход на главную страницу
    # include(main.urls) - также вызываем файл urls который находится в папке main
]
