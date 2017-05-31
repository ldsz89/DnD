from django.conf.urls import url

from . import views

app_name = 'playermanager'

urlpatterns = [
    # /playermanager/
    url(r'^$', views.dashboard, name='dashboard'),
    # /playermanager/<character_id>/
    url(r'^(?P<character_id>[0-9]+)/$', views.detail, name='detail'),
]
