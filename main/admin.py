from django.contrib import admin
from .models import *
admin.site.register(ExtraInfo)
admin.site.register(Movie)
admin.site.register(Review)



# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     #fields = ('name', 'description') co chcemy miec wyswietlane w srodku
#     list_display = ('name', 'year', 'description', 'imdb_rating')
#     list_filter = ('year', 'released')
#     search_fields = ('name', 'description')
#
# @admin.register(ExtraInfo)
# class MoreInfoAdmin(admin.ModelAdmin):
#     list_display = ('rodzaj',)
#


