from django.urls import path
from django.conf.urls import url, include
from . import views
from appLibreria.views import Index, ColeccionList, AutorList, TagList, AutorDetail, ComicDetail, ColeccionDetail, PageView

urlpatterns = [
 url(r'^i18n/', include('django.conf.urls.i18n')),
 path('comics/', Index.as_view(), name='index'),
 path('colecciones/', ColeccionList.as_view(), name='coleccionList'),
 path('autores/', AutorList.as_view(), name='autorList'),
 path('tags/', TagList.as_view(), name='tagList'),
 path('autor/<int:pk>/', AutorDetail.as_view(), name='autorDetail'),
 path('comic/<int:pk>/', ComicDetail.as_view(), name='comicDetail'),
 path('coleccion/<int:pk>/', ColeccionDetail.as_view(), name='coleccionDetail'),
 path('comic/<int:pk>/numeroPaginahelp', PageView.as_view(), name='pageView'),#Próximamente con JS
]