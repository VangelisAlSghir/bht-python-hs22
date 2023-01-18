from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('show/', views.movie_list, name='movies-list'),
    path('show/<int:pk>/', views.movie_detail, name='movies-detail'),
    path('show/<int:pk>/vote/<int:pk_comment>/<str:up_or_down>/', views.vote, name='comment-vote'),
    path('delete/<int:pk>/', views.movie_delete, name='movies-delete'),
    path('add/', views.movie_create, name='movies-create'),
    path('edit/<int:pk>', views.movie_edit, name='movies-edit'),
    path('report/<int:pk>/<int:pk_comment>', views.report_product_review, name='report-review'),
    path('review/delete/<int:pk>/<int:pk_comment>', views.delete_product_review, name='delete-review'),
    path('review/edit/<int:pk>/<int:pk_comment>', views.edit_review, name='edit-review'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]