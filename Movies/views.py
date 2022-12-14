from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from Movies.forms import MovieForm, ProductReviewForm
from Movies.models import Movie, ProductReview, Vote


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = { 'movies': movies }
    return render(request, 'movies-list.html', context)


def movie_detail(request, **kwargs):
    movie_id = kwargs['pk']
    selected_movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        form.instance.user = request.user
        form.instance.movie = selected_movie
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = ProductReview.objects.filter(movie=selected_movie)

    context = {
        'selected_movie': selected_movie,
        'selected_movie_comments': comments,
        'comment_form': ProductReviewForm
    }
    return render(request, 'movies-detail.html', context)


def movie_create(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('movies-list')

    if request.method == 'POST':
        filled_form = MovieForm(request.POST, request.FILES)
        filled_form.instance.user = request.user
        filled_form.creation_date = date.today()
        filled_form.fsk = int(request.POST['fsk'])
        if filled_form.is_valid():
            # filled_form.image = request.FILES['image']
            # filled_form.pdf = request.FILES['pdf']
            filled_form.save()
        else:
            pass

        return redirect('movies-list')
    else:
        empty_form = MovieForm()
        fsk = Movie.FSK_CATEGORIES
        context = {'form': empty_form, 'fsk_categories': fsk}
        return render(request, 'movies-create.html', context)


def movie_delete(request, **kwargs):
    movie_id = kwargs['pk']
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('movies-list')

    if request.method == 'POST':
        Movie.objects.get(id=movie_id).delete()
        return redirect('movies-list')
    else:
        selected_movie = Movie.objects.get(id=movie_id)
        context = {'selected_movie': selected_movie}
        return render(request, 'movies-delete.html', context)


def vote(request, pk: str, pk_comment: str, up_or_down: str):
    comment = ProductReview.objects.get(id=int(pk_comment))
    user = request.user
    try:
        existing_vote = Vote.objects.get(user=user, comment=comment)
    except Vote.DoesNotExist:
        existing_vote = None

    if existing_vote is None:
        comment.vote(user, up_or_down)
    else:
        if existing_vote.has_same_answer(up_or_down):
            existing_vote.delete()
        else:
            existing_vote.delete()
            comment.vote(user, up_or_down)

    return redirect('movies-detail', pk=pk)