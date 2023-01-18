from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Movies.forms import MovieForm, ProductReviewForm
from Shoppingcart.models import ShoppingCart
from Movies.models import Movie, ProductReview, Vote

from django.views.generic import TemplateView, ListView
from django.db.models import Q




# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    context = { 'movies': movies }
    return render(request, 'movies-list.html', context)


def movie_detail(request, **kwargs):
    movie_id = kwargs['pk']
    selected_movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST' and 'add_comment' in request.POST:
        form = ProductReviewForm(request.POST)
        form.instance.user = request.user
        form.instance.movie = selected_movie

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    # Add to shopping cart
    if request.method == 'POST' and 'add_to_cart' in request.POST:
        myuser = request.user
        ShoppingCart.add_item(myuser, selected_movie)

    reviews = ProductReview.objects.filter(movie=selected_movie, deleted=False)

    if request.user.is_authenticated:
        user_has_rated = reviews.filter(user=request.user).count() > 0
    else:
        user_has_rated = True

    context = {
        'selected_movie': selected_movie,
        'selected_movie_reviews': reviews,
        'comment_form': ProductReviewForm,
        'user_has_rated': user_has_rated,
        'current_user_id': request.user.id
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

def movie_edit(request, **kwargs):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('movies-list')

    movie_id = kwargs['pk']

    movie = Movie.objects.get(id=movie_id)

    if request.method == 'POST':
        filled_form = MovieForm(request.POST, request.FILES, instance=movie)
        if filled_form.is_valid():
            filled_form.save()
        else:
            pass

        return redirect('movies-list')
    else:
        empty_form = MovieForm(instance=movie)
        fsk = Movie.FSK_CATEGORIES
        context = {'form': empty_form, 'fsk_categories': fsk}
        return render(request, 'movies-edit.html', context)


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
        existing_vote = Vote.objects.get(user=user, productReview=comment)
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


def report_product_review(request, pk: str, pk_comment: str):
    comment = ProductReview.objects.get(id=int(pk_comment))

    comment.reported = True
    comment.save()

    return render(request, 'movies-reported.html', {'pk': pk})


def delete_product_review(request, pk: str, pk_comment: str):
    comment = ProductReview.objects.get(id=int(pk_comment))

    comment.deleted = True
    comment.save()

    return render(request, 'movie-review-deleted.html', {'pk': pk})


def edit_review(request, pk: str, pk_comment: str):
    comment = ProductReview.objects.get(id=int(pk_comment))

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=comment)
        form.save()

        return redirect('movies-detail', pk)
    else:
        form = ProductReviewForm(instance=comment)
        context = {'form': form}
        return render(request, 'edit-review.html', context)


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("eingabe")
        object_list = Movie.objects.filter(Q(name__icontains=query))

        return object_list


