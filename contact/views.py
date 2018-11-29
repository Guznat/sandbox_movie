from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.views import View


class EmailView(View):
    def get(self, request):
        form = ContactForm()
        ctx = {
            'form': form
        }
        return render(request, 'contact_form.html', ctx)

    def post(self, request):
        form = ContactForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, message, from_email, ['mojdjango@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
        return render(request, 'contact_form.html', ctx)

