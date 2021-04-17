from django.contrib import admin
from django.urls import path
from DJ_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
    path('info/', views.showInfo)
]
