from django.conf.urls import url

from . import views

app_name = 'ccreator'

urlpatterns = [
    # /ccreator/character/add/
    url(r'^character/add/$', views.CharacterCreate.as_view(), name='character-add'),
    # /ccreator/update/<character_id>/
    url(r'^character/update/(?P<pk>[0-9]+)/$', views.CharacterUpdate.as_view(), name='character-update'),
    # /ccreator/<character_id>/delete/
    # url(r'^character/(?P<pk>[0-9]+)/delete/$', views.CharacterDelete.as_view(), name='character-delete'),
    url(r'^character/(?P<pk>[0-9]+)/delete/$', views.character_delete, name='character-delete'),
]
