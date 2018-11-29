from django.urls import path
from main.views import *


urlpatterns = [
    path('filmy/', wszystkie_filmy, name='wszystkie_filmy'),
    path('filmyy/', filmy),
    path('new/', nowy_film, name='nowy_film'),
    path('edit/<int:id>/', edytuj_film, name='edytuj_film'),
    path('delete/<int:id>/', usun_film, name='usun_film'),
    path('film/<int:id>/', film_idd, name='film_id'),
    # path('extrainfo/', nowe_extra_info, name='extrainfo'),
    path('extrainfo/<int:id>/', edytuj_extra_info, name='editextrainfo'),
    path('form_rev/<int:movie_id>', review_form, name='form_rev')
]
