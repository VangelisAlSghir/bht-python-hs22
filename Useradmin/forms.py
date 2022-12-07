from django import forms

from Useradmin.models import DefaultUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = DefaultUser
        fields = ['username', 'password', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
