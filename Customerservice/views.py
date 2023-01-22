from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .forms import CommentEditForm
from Movies.models import ProductReview
from Movies.models import Movie


class ReportedDeleteView(ListView):
    model = ProductReview
    context_object_name = 'all_the_reviews'
    template_name = 'reported-reviews-delete.html'

    def get_context_data(self, **kwargs):
        context = super(ReportedDeleteView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        if not user.is_anonymous:
            can_delete = user.can_delete()
        context['can_delete'] = can_delete
        return context

    def post(self, request, *args, **kwargs):
        review_id = request.POST['review_id']
        if 'delete' in request.POST:
            ProductReview.objects.get(id=review_id).delete()
            return redirect('review-delete')


class ReviewDeleteView(ListView):
    model = ProductReview
    context_object_name = 'all_the_reviews'
    template_name = 'review-delete.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewDeleteView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        if not user.is_anonymous:
            can_delete = user.can_delete()
        context['can_delete'] = can_delete
        return context

    def post(self, request, *args, **kwargs):
        review_id = request.POST['review_id']
        if 'delete' in request.POST:
            ProductReview.objects.get(id=review_id).delete()
            return redirect('comment-delete')


class MovieDeleteView(ListView):
    model = Movie
    context_object_name = 'all_the_movies'
    template_name = 'movie-edit-delete.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDeleteView, self).get_context_data(**kwargs)
        can_delete = False
        user = self.request.user
        if not user.is_anonymous:
            can_delete = user.can_delete()
        context['can_delete'] = can_delete
        return context

    def post(self, request, *args, **kwargs):
        movie_id = request.POST['movie_id']
        if 'delete' in request.POST:
            return redirect('movies-delete', movie_id)
