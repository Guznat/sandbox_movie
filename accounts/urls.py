from django.conf.urls import url
from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path('signup/', accounts_views.AddUserView.as_view(), name='signup'),
    path('listusers/', accounts_views.ListUsers.as_view(), name='listusers'),
    path('profile/(<int:id>)', accounts_views.user_profile, name='profile'),
#TODO profile zamiast wyswietlac zalogowanego loguje automatycnie na wskazanego uzytkownika
]