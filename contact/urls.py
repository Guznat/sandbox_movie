from django.contrib import admin
from django.urls import path
from contact import views as contact_view




urlpatterns = [
    path('contact/', contact_view.EmailView.as_view(), name='contact')
]