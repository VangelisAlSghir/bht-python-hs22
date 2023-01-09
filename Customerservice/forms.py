from django import forms
from Movies.models import ProductReview


class CommentEditForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ['text']
        widgets = {
            'comment_id': forms.HiddenInput(),
        }