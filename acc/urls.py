from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<entry>/', views.delete_entry, name='delete_entry'),
    path('edit/<id>/', views.edit_entry, name='edit_entry'),
    path('tasks/', views.Tasks, name='Tasks'),
    path('delete_task/<task>/', views.delete_task, name='delete_task'),
    path('cross/<id>/', views.cross, name='cross'),
    path('uncross/<id>/', views.uncross, name='uncross'),
    path('Edit/<id>/', views.edit, name='edit'),
]