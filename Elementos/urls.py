from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('buscar/', buscar),
    path('detail/', detail),
    path('list/', ElementosList.as_view()),
    path('list/asc/', ListOrdenAsc().as_view()),
    path('list/desc/', ListOrdenDesc().as_view()),
    path('list/noatomico/', ListNoAtomico().as_view()),
    path('create/', ElementoCreate.as_view()),
    re_path('^detail/(?P<nombre>.+)/$', ElementoDetail.as_view()),
    re_path('^delete/(?P<nombre>.+)/$', ElementoDelete.as_view()),
    re_path('^update/(?P<nombre>.+)/$', ElementoUpdate.as_view()),
    path('categoria/', CategoriaList.as_view()),
    path('filter/', ElementoListFilter.as_view()),
    #path('categoria/create/', CategoriaCreate.as_view()),
    #path('periodo/create/', PeriodoCreate.as_view()),
    #path('grupo/create/', GrupoCreate.as_view()),
    path('grupo/', ListGrupo.as_view()),
    path('periodo/', ListPeriodo.as_view()),
]