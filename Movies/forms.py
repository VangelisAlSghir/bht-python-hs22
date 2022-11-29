from django import forms
from .models import Movie, ProductReview


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'description', 'fsk', 'image', 'pdf', 'price', 'creation_date']
        widgets = {
            'fsk': forms.Select(choices=Movie.FSK_CATEGORIES),
            'user_id': forms.HiddenInput(),
        }


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'movie': forms.HiddenInput(),
        }