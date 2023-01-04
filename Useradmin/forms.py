from django import forms

from Useradmin.models import DefaultUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = DefaultUser
        fields = ['username', 'password', 'image']
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditUserForm(forms.ModelForm):
    new_password = forms.PasswordInput()

    class Meta:
        model = DefaultUser
        fields = ['image']
        widgets = {
            'user_id': forms.HiddenInput(),
        }

