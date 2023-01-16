from django import forms
from .models import Movie, ProductReview


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'genre', 'fsk', 'image', 'pdf', 'price']
        widgets = {
            'fsk': forms.Select(choices=Movie.FSK_CATEGORIES),
            'genre': forms.Select(choices=Movie.GENRES),
            'user_id': forms.HiddenInput(),
            'creation_date': forms.HiddenInput()
        }


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['text', 'rating']
        widgets = {
            'user': forms.HiddenInput(),
            'movie': forms.HiddenInput(),
        }
