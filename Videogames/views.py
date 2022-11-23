from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from Videogames.forms import VideogameForm, CommentForm
from Videogames.models import Videogame, Comment, Vote


# Create your views here.
def videogame_list(request):
    games = Videogame.objects.all()
    context = { 'videogames': games }
    return render(request, 'videogame-list.html', context)


def videogame_detail(request, **kwargs):
    videogame_id = kwargs['pk']
    selected_game = Videogame.objects.get(id=videogame_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.videogame = selected_game
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(videogame=selected_game)

    context = {
        'selected_game': selected_game,
        'selected_game_comments': comments,
        'comment_form': CommentForm
    }
    return render(request, 'videogame-detail.html', context)


def videogame_create(request):
    if request.method == 'POST':
        filled_form = VideogameForm(request.POST)
        filled_form.instance.user = request.user
        if filled_form.is_valid():
            filled_form.save()
        else:
            pass

        return redirect('videogame-list')
    else:
        empty_form = VideogameForm()
        fsk = Videogame.FSK_CATEGORIES
        genre = Videogame.GAME_GENRES
        context = {'form': empty_form, 'fsk': fsk, 'genre': genre}
        return render(request, 'videogame-create.html', context)


def videogame_delete(request, **kwargs):
    videogame_id = kwargs['pk']
    if request.method == 'POST':
        Videogame.objects.get(id=videogame_id).delete()
        return redirect('videogame-list')
    else:
        selected_game = Videogame.objects.get(id=videogame_id)
        context = {'selected_game': selected_game}
        return render(request, 'videogame-delete.html', context)


def vote(request, pk: str, pk_comment: str, up_or_down: str):
    comment = Comment.objects.get(id=int(pk_comment))
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

    return redirect('videogame-detail', pk=pk)