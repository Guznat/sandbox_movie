from django.forms import ModelForm
from .models import Movie, ExtraInfo, Review
from django import forms


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
        fields = ['name', 'description', 'year', 'imdb_rating','released', 'photo']



# class MovieForm(forms.Form):
#     name = forms.CharField(max_length=24)
#     description = forms.CharField(max_length=48, widget=forms.Textarea)
#     year = forms.IntegerField(max_value=2025, min_value=1895)
#     imdb_rating = forms.DecimalField(max_digits=3, decimal_places=2, widget=forms.NumberInput)
#     released = forms.DateField(widget=forms.SelectDateWidget(years=range(1895, 2025)))
#     photo = forms.ImageField()
#
#     def clean(self):
#         data = self.cleaned_data
#         if Movie.objects.filter(name=data['name']):
#             raise forms.ValidationError('Movie already exist')
#         return data
#TODO Formy fajnie dzialaja ale tylko na nowym filmie, nie dziala opcja   instance=film



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['nick', 'text', 'stars', 'movie']





