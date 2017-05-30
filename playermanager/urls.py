from django.conf.urls import url

from . import views

urlpatterns = [
    # /playermanager/
    url(r'^$', views.dashboard, name='dashboard'),
    # /playermanager/1/
    url(r'^(?P<character_id>[0-9]+)/$', views.detail, name='detail'),
]
