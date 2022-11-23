from datetime import date

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Videogame(models.Model):
    GAME_GENRES = [
        ('FPS', 'First-Person Shooter'),  # Wert und lesbare Form
        ('S', 'Strategie'),
        ('A', 'Adventure'),
        ('MOBA', 'Multiplayer Online Battle Arena'),
        ('RPG', 'Rollenspiel'),
        ('R', 'Rätsel'),
        ('Sp', 'Sport'),
        ('TPS', 'Third-Person Shooter'),
        ('JnR', 'Jump and Run')
    ]

    FSK_CATEGORIES = [
        (0, 'ab 0'),
        (6, 'ab 6'),
        (12, 'ab 12'),
        (16, 'ab 16'),
        (18, 'ab 18'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,
                                blank=True)
    genre = models.CharField(max_length=4,
                             choices=GAME_GENRES)
    fsk = models.IntegerField(choices=FSK_CATEGORIES)
    creation_date = models.DateField(default=date.today)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta:
        verbose_name = 'VideoGame'
        verbose_name_plural = 'VideoGames'

    def __str__(self):
        return self.name + ' (' + self.user + ')'

    def __repr__(self):
        return self.name + ' / ' + self.user + ' / ' + self.creation_date


class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def vote(self, user, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'

        vote = Vote.objects.create(up_or_down=U_or_D,
                                   user=user,
                                   comment=self
                                   )

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='U',
                                      comment=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='D',
                                        comment=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + str(self.timestamp) + ')'


class Vote(models.Model):
    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    up_or_down = models.CharField(max_length=1,
                                  choices=VOTE_TYPES,
                                 )
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def has_same_answer(self, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'

        return self.up_or_down == U_or_D

    def __str__(self):
        return self.up_or_down + ' on ' + self.comment.videogame.name + ' by ' + self.user.username
