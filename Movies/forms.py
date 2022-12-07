from django import forms
from .models import Movie, ProductReview

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'fsk', 'price']
        widgets = {
            'fsk': forms.Select(choices=Movie.FSK_CATEGORIES),
            # 'image': forms.FileField(),
            # 'pdf': forms.FileField(),
            'user_id': forms.HiddenInput(),
            'creation_date': forms.HiddenInput()
        }


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'movie': forms.HiddenInput(),
        }
