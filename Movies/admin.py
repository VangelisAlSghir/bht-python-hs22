from django.contrib import admin

from Movies.models import Movie, ProductReview, Vote

# Register your models here.
admin.site.register(Movie)
admin.site.register(ProductReview)
admin.site.register(Vote)
