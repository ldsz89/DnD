from django.conf.urls import url

from . import views

app_name = 'ccreator'

urlpatterns = [
    # /ccreator/
    url(r'^$', views.index, name='index'),
    # /ccreator/<character_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.EditView.as_view(), name='edit'),
    # /ccreator/character/add/
    url(r'^character/add/$', views.CharacterCreate.as_view(), name='character-add')
]
