from django.urls import reverse_lazy
from django.views import generic

from Useradmin.forms import RegisterForm


class SignUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'