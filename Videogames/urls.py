from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.videogame_list, name='videogame-list'),
    path('show/<int:pk>/', views.videogame_detail, name='videogame-detail'),
    path('show/<int:pk>/vote/<int:pk_comment>/<str:up_or_down>/', views.vote, name='comment-vote'),
    path('delete/<int:pk>/', views.videogame_delete, name='videogame-delete'),
    path('add/', views.videogame_create, name='videogame-create'),
]