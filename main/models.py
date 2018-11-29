from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


RODZAJE = {
    (0, "Nieznany"),
    (1, "Horror"),
    (2, "Drama"),
    (3, "Comedy"),
    (4, "Sci-fi"),
    (5, "Thiller"),
    (6, "Fantasy"),
    (7, "Document"),
}


class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name) + " (" + str(self.year) + ")"


class ExtraInfo(models.Model):
    czas_trwnia = models.IntegerField(default=0)
    rodzaj = models.IntegerField(choices=RODZAJE, default=0)
    movie = AutoOneToOneField(Movie, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.czas_and_rodzaj()

    def czas_and_rodzaj(self):
        return str(self.movie) + "  " + str(self.czas_trwnia) + "min   rodzaj filmu:" + str(self.rodzaj)


class Review(models.Model):
    nick = models.CharField(max_length=100, null=False, default="")
    text = models.CharField(default='', blank=True, max_length=260)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateTimeField(default=timezone.now)
    movie = models.ForeignKey('main.Movie', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.nick_i_movie()

    def nick_i_movie(self):
        return f"{self.nick} dodał komentarz do {self.movie}."