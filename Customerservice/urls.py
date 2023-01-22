from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
    path('home/', TemplateView.as_view(template_name='customerservice-home.html'), name='customerservice-home'),
    path('reported-delete/', views.ReportedDeleteView.as_view(), name='reported-reviews-delete'),
    path('movie-delte/', views.MovieDeleteView.as_view(), name='movie-delete-list'),
]