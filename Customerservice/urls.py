from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('edit/<int:pk>/', views.CommentEditView.as_view(), name='comment-edit'),
    path('editdelete/<int:pk>/', views.comment_edit_delete, name='comment-edit-delete'),
    path('home/', TemplateView.as_view(template_name='customerservice-home.html'), name='customerservice-home'),
    path('reported-delete/', TemplateView.as_view(template_name='reported-comments-delete.html'), name='reported-comments-delete'),
]