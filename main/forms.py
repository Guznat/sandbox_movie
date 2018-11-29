from django.forms import ModelForm
from .models import Movie, ExtraInfo, Review


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwnia', 'rodzaj', 'movie']


class ExtraInfoEditForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['czas_trwnia', 'rodzaj']


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'released', 'imdb_rating', 'photo']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['nick', 'text', 'stars', 'movie']
