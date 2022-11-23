from django import forms
from .models import Videogame, Comment


class VideogameForm(forms.ModelForm):

    class Meta:
        model = Videogame
        fields = ['name', 'description', 'genre', 'fsk', 'creation_date']
        widgets = {
            'genre': forms.Select(choices=Videogame.GAME_GENRES),
            'fsk': forms.Select(choices=Videogame.FSK_CATEGORIES),
            'user_id': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'videogame': forms.HiddenInput(),
        }
