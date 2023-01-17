from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit-user/', views.edit_user, name='edit-user'),
    path('logout/', views.logout_page, name='logout'),
]