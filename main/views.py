from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, ExtraInfo, Review
from .forms import MovieForm, ExtraInfoForm, ExtraInfoEditForm, ReviewForm
from django.contrib.auth.decorators import login_required
from random import choice
from meows.forms import MeowModelForm

from django.views import View


# from django.core.mail import send_mail, BadHeaderError
# from contact.forms import ContactForm


def filmy(request):
    filmsy = ['Terminator', 'O dwoch takich co ukradli ksieżyc']
    ctx = {
        'filmy': filmsy
    }
    return render(request, 'filmy.html', ctx)


#                       Film profile view <--------------------
def film_idd(request, id):
    film = get_object_or_404(Movie, pk=id)
    info = get_object_or_404(ExtraInfo, pk=id)
    rodzaj = ExtraInfoForm(request.POST)
    comment = Review.objects.filter(movie_id=id)
    # TODO spytac sie dlaczego dziala

    ctx = {

        'film': film,
        'info': info,
        'rodzaj': rodzaj,
        'comment': comment,

    }
    if rodzaj.is_valid():
        rodzaj.save()
        redirect(film)
    return render(request, 'film.html', ctx)


#                coments form view <----------------
@login_required
def review_form(request, movie_id):
    form_rev = ReviewForm(request.POST or None)
    ctx = {
        'form_rev': form_rev
    }
    if form_rev.is_valid():
        form_rev.save()
        return redirect(wszystkie_filmy)

    return render(request, 'reviewform.html', ctx)


# TODO Nowy komentarz, jak autouzupelnic movie_id

#               New extra info view <-----------------
@login_required
def nowe_extra_info(request):
    form = ExtraInfoForm(request.POST or None)
    ctx = {
        'form': form,
    }
    if form.is_valid():
        form.save()
    return render(request, 'extrainfoform.html', ctx)


#                    edit extra info view <-----------------
@login_required
def edytuj_extra_info(request, id):
    info = get_object_or_404(ExtraInfo, pk=id)
    form = ExtraInfoEditForm(request.POST or None, instance=info)
    # instance wyciagnie juz istniejace dane z bazy danych i wsadzi
    #  do formularza celem edytowania
    ctx = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'extrainfoformedit.html', ctx)


# TODO problem z redirectem, nie wiem jak wrocic do  filmu(id)


#                     All film view <----------------------
def wszystkie_filmy(request):
    filmiki = Movie.objects.all()

    ctx = {
        'text': filmiki

    }

    return render(request, 'lista_filmow.html', ctx)


#                      new film form <-----------------
@login_required
def nowy_film(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    ctx = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'film_form.html', ctx)


# TODO Zapytać sie o nowy film + nowe extra info na tym samym template
#  ( wywala blad po stworzeniu filmu gdy chce sie wejsc na jego strone )


#                           edit film view <---------------
@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Movie, pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=film)
    # instance wyciagnie juz istniejace dane z bazy danych i wsadzi
    #  do formularza celem edytowania
    ctx = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
    return render(request, 'film_form.html', ctx)


#                         delete film view <-------------------
@login_required
def usun_film(request, id):
    film = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        film.delete()
        return redirect(wszystkie_filmy)
    return render(request, 'potwierdz.html', {'film': film})


#                              homepage view <-------------------
class Homepage(View):
    def get(self, request):
        list = ['When your photo is taken for your driver’s license, why do they tell you to smile?',
                'If you are stopped by the police and asked for your license, are you going to be smiling?',
                'If you undergo chemotherapy do you lose your body hair?',
                'Do married people really live longer than single people, or does it just seem longer?',
                'Why does toilet bowl cleaner only come in the colour blue?',
                'Why do ‘fat chance’ and ‘slim chance’ mean the same thing?',
                'Do the Alphabet song and Twinkle, Twinkle Little Star have the same tune?',
                'If you put a chameleon in a room full of mirrors, what colour would it turn?',
                'With so many rivers running into the ocean, why doesn’t the water level rise?',
                'If a vacuum cleaner really sucks, is that good or bad?',
                'What are the handles for corn on the cob called?',
                'When bald people wash their face, how far up do they go?',
                ]
        zdanko = choice(list)

        ctx = {
            'zdanie': zdanko
        }
        return render(request, 'homepage.html', ctx)
    def post(self, request):
        form = MeowModelForm(request.POST or None)
        ctx = {'form':'form'}
        if form.is_valid():
            form.save()
        return render(request, 'homepage.html', ctx)


# Contactform w stopce
# class FooterView(View):
#     def get(self, request):
#         form = ContactForm()
#         ctx = {
#             'form': form
#         }
#         return render(request, 'footer.html', ctx)
#
#     def post(self, request):
#         form = ContactForm(request.POST)
#         ctx = {
#             'form': form
#         }
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             from_email = form.cleaned_data['from_email']
#             try:
#                 send_mail(subject, message, from_email, ['mojdjango@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#         return render(request, 'footer.html', ctx)


# widoki generyczne ogarnać!!!


# @login_required
# def nowy_film(request):
#     form = MovieForm(request.POST or None, request.FILES or None)
#     ctx = {
#         'form': form,
#     }
#     if form.is_valid():
#         movie = Movie.objects.create(
#             name = form.cleaned_data['name'],
#             description = form.cleaned_data['description'],
#             year = form.cleaned_data['year'],
#             imdb_rating = form.cleaned_data['imdb_rating'],
#             released = form.cleaned_data['released'],
#             photo = form.cleaned_data['photo'],
#             )
#         movie.save()
#         return redirect(wszystkie_filmy)
#     return render(request, 'film_form.html', ctx)
