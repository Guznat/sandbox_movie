from django import forms

from .models import Meow, ReplyMeow


class MeowModelForm(forms.ModelForm):
    class Meta:
        model = Meow
        fields = [
            #'user',
            'content']

class   MeowReplyModelForm(forms.ModelForm):
    class Meta:
        model = ReplyMeow
        fields = [
            #'meow',
            'content'
         ]

