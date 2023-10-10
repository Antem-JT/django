from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('create-notes', views.CreateNote, name='create'),
    path('read-notes/<str:pk>', views.ReadNote, name='read'),
    path('delete-notes/<str:pk>', views.DeleteNote, name='delete'),
    path('edit-notes/<str:pk>', views.EditNote, name='edit'),
]
