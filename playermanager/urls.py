from django.conf.urls import url

from . import views

app_name = 'playermanager'

urlpatterns = [
    # /playermanager/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /playermanager/login/
    url(r'^login/$', views.login_view, name='login'),
    # /playermanager/login/
    url(r'^logout/$', views.UserLogoutView.as_view(), name='logout'),
    # /playermanager/
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    # /playermanager/characers/
    url(r'^characters/$', views.CharacterView.as_view(), name='characters'),
    # /playermanager/<character_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
