from django.urls import path

import Customerservice
import Movies
from . import views
from django.views.generic import TemplateView
from Movies import views

urlpatterns = [
    path('delete/', Customerservice.views.ReviewDeleteView.as_view(), name='review-delete'),
    path('home/', TemplateView.as_view(template_name='customerservice-home.html'), name='customerservice-home'),
    path('reported-delete/', Customerservice.views.ReportedDeleteView.as_view(), name='reported-reviews-delete'),
    path('movie-edit-delete/', Customerservice.views.MovieDeleteView.as_view(), name='movie-edit-delete'),
    path('movie-edit/<int:pk>', Movies.views.movie_edit, name='movie-edit'),
]