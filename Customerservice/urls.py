from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    path('home/', TemplateView.as_view(template_name='customerservice-home.html'), name='customerservice-home'),
    path('reported-delete/', views.ReportedDeleteView.as_view(), name='reported-comments-delete'),
]