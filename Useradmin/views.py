from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from Useradmin.forms import RegisterForm, EditUserForm
from Useradmin.models import DefaultUser


class SignUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def edit_user(request, **kwargs):
    current_user = DefaultUser.objects.get(id=request.user.id)

    if request.method == 'POST':
        filled_form = EditUserForm(request.POST, request.FILES, instance=current_user)
        if request.POST['new_password'] != "":
            current_user.set_password(request.POST['new_password'])
        filled_form.save()

        return redirect('home')
    else:
        empty_form = EditUserForm(instance=current_user)

        context = {'form': empty_form, 'image': current_user.image}
        return render(request, 'edit-user.html', context)


