from datetime import date

from django.contrib.auth.models import User
from django.db import models

from Useradmin.models import DefaultUser


# Create your models here.
class Movie(models.Model):
    FSK_CATEGORIES = [
        (0, 'ab 0'),
        (6, 'ab 6'),
        (12, 'ab 12'),
        (16, 'ab 16'),
        (18, 'ab 18'),
    ]
    GENRES = [
        ('H', 'Horror'),
        ('F', 'Familienfilm'),
        ('A', 'Action'),
        ('S', 'Superhelden'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,
                                blank=True)
    fsk = models.IntegerField(choices=FSK_CATEGORIES)
    genre = models.CharField(choices=GENRES,
                             max_length=1)
    price = models.FloatField()
    image = models.FileField(upload_to="movies/images/", blank=True)
    pdf = models.FileField(upload_to="movies/pdf/", blank=True)
    creation_date = models.DateField(default=date.today)
    user = models.ForeignKey(DefaultUser,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    def __str__(self):
        return self.name + ' (' + self.user + ')'

    def __repr__(self):
        return self.name + ' / ' + self.user + ' / ' + self.creation_date


class ProductReview(models.Model):
    text = models.TextField(max_length=500)
    rating = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(DefaultUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    deleted = models.BinaryField()
    reported = models.BinaryField()

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'ProductReview'
        verbose_name_plural = 'ProductReviews'

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
    user = models.ForeignKey(DefaultUser, on_delete=models.CASCADE)
    productReview = models.ForeignKey(ProductReview, on_delete=models.CASCADE)

    def has_same_answer(self, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'

        return self.up_or_down == U_or_D

    def __str__(self):
        return self.up_or_down + ' on ' + self.productReview.movie.name + ' by ' + self.user.username
