from django.urls import path
from . import views

urlpatterns=[

    path('',views.temp,name='temp'),
    path('taskspec/<str:pk>/',views.taskspec,name='taskspec'),
    path('upload/',views.upload,name='upload'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),


]