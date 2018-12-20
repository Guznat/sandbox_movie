from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meow
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import MeowModelForm
from django.contrib.auth.decorators import login_required
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.urls import reverse_lazy
from django.db.models import Q


class MeowCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Meow.objects.all()
    # fields = ['user', 'content']
    template_name = 'meows/meow_create.html'
    form_class = MeowModelForm
    #success_url = reverse_lazy("meow:meow_detail") #dodano bezposrednio do modelu Meow
    login_url = 'login'

    # przeniesione do mixina
    # def form_valid(self, form):
    #     if self.request.user.is_authenticated:
    #         form.instance.user = self.request.user
    #         return super(MeowCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You must be login!"])
    #         return self.form_invalid(form) #retur redirect('login')


# wersja z funkcja
# def meow_create_view(request):
#     form = MeowModelForm(request.POST or None)
#     ctx = {
#         'form':form
#     }
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#
#     return render(request, "meows/meow_create.html",ctx)

class MeowUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Meow.objects.all()
    form_class = MeowModelForm
    template_name = 'meows/meow_update.html'
    # success_url = '/meow/' #dodano bezposrednio do modelu Meow

class MeowDeleteView(LoginRequiredMixin,UserOwnerMixin, DeleteView):
    model = Meow
    template_name = 'meows/meow_delete.html'
    success_url = reverse_lazy('meows_list') #reverse()


class MeowDetailView(DetailView):
    queryset = Meow.objects.all()
    template_name = "meows/meow_detail.html"

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     object = Meow.objects.get(id=pk)
    #     return  object


# def meow_detail_view(request, id):
#     meow = get_object_or_404(Meow, pk=id)
#     ctx = {
#        'meow':meow
#     }
#   return render(request,"meows/meow_detail.html', ctx)

class MeowListView(ListView):
    template_name = "meows/meow_list.html"
    # queryset = Meow.objects.all().order_by("-add_date")

    def get_queryset(self, *args, **kwargs):
        qs = Meow.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )

        return qs.order_by("-add_date")

# def meow_list_view(request):
#     meows = Meow.objects.all().order_by('add_date')
#     ctx={
#         'meows':meows
#     }
#     return render(request, 'meows/meow_list.html', ctx)

# class ReplyCreateView(CreateView):
#     template_name =