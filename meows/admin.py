from django.contrib import admin
from .models import Meow
from .forms import MeowModelForm


# admin.site.register(Meow)


class MeowModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Meow


admin.site.register(Meow)
