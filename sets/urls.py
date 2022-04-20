from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('flashcard_delete/<flashcard_id>/', views.flashcard_delete, name='flashcard_delete'),
    path('set_create/', views.set_create, name='set_create'),
    path('flashcard_delete/<flashcard_id>/', views.flashcard_delete, name='set_delete'),
    path('learn/<learn_id>', views.learn, name='learn'),
    path('flashcard_list/<flashcard_id>', views.flashcard_list, name='flashcard_list')
]
