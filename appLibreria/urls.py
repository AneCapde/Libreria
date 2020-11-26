from django.urls import path
from appLibreria.views import Index, ColeccionList, AutorList, TagList, AutorDetail, ComicDetail, ColeccionDetail, PageView

urlpatterns = [
 path('index', Index.as_view(), name='index'),
 path('colecciones', ColeccionList.as_view(), name='coleccionList'),
 path('autores', AutorList.as_view(), name='autorList'),
 path('tags', TagList.as_view(), name='tagList'),
 path('autor/nombreautorhelp', AutorDetail.as_view(), name='autorDetail'),
 path('comic/nombrecomichelp', ComicDetail.as_view(), name='comicDetail'),
 path('coleccion/nombrecoleccionhelp', ColeccionDetail.as_view(), name='coleccionDetail'),
 path('comic/nombrecomichelp/numeroPaginahelp', PageView.as_view(), name='pageView'),
]