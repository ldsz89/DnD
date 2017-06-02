from django.conf.urls import url

from . import views

app_name = 'playermanager'

urlpatterns = [
    # /playermanager/
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    # /playermanager/characers/
    url(r'^characters/$', views.CharacterView.as_view(), name='characters'),
    # /playermanager/<character_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
