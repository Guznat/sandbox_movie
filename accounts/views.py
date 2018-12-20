from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.models import User
from accounts import forms as account_forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# def signup(request):
#     form = UserCreationForm(request.POST)
#     ctx = {
#         'form': form
#     }
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect(reverse('homepage'))
#         else:
#             return render(request, 'registration/signup.html', {'form': UserCreationForm() })
#     else:
#         return render(request, 'registration/signup.html', ctx)

# NIE RYRA
#                        Add User view <-----------
class AddUserView(View):
    def get(self, request):
        form = account_forms.CreateUserForm()
        ctx = {
            'form': form
        }
        return render(request, 'registration/signup.html', ctx)

    def post(self, request):
        form = account_forms.CreateUserForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            login(request, user)
            return redirect(reverse('homepage'))
        return render(request, 'registration/signup.html', ctx)


#                    User List view <--------------
class ListUsers(View):
    def get(self, request):
        ctx = {
            'users': User.objects.all()
        }
        return render(request, 'registration/listusers.html', ctx)


#                   User Profile view <-------------
@login_required
def user_profile(request, id):
    user = User.objects.get(pk=id)
    return render(request, 'registration/user_profile.html', {"user": user})
