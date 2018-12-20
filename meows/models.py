from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .validators import validate_content


class Meow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=240, validators=[validate_content])
    add_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content) + "(" + str(self.id) + ")"

    def get_absolute_url(self):
        return reverse("meow_detail", kwargs={"pk": self.pk})

    # def clean(self, *args, **kwargs):        #Validator
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError('Cannot be abc')
    #     return content


class ReplyMeow(models.Model):
    meow = models.ForeignKey(Meow, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=240, validators=[validate_content])
    add_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("meow_detail", kwargs={"pk": self.pk})
