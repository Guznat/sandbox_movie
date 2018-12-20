from django.urls import path
from .views import MeowDetailView, MeowListView, MeowCreateView, MeowUpdateView, MeowDeleteView
from django.conf.urls import url




urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MeowDetailView.as_view(), name='meow_detail'),
    url(r'^(?P<pk>\d+)/update$', MeowUpdateView.as_view(), name='meow_update'),
    url(r'^(?P<pk>\d+)/delete$', MeowDeleteView.as_view(), name='meow_delete'),
    path('', MeowListView.as_view(), name='meows_list'),
    path('create/', MeowCreateView.as_view(), name='create_meow')
]