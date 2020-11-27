from django.urls import path
from appLibreria.views import Index, ColeccionList, AutorList, TagList, AutorDetail, ComicDetail, ColeccionDetail, PageView, Prueba

urlpatterns = [
 path('comics/', Index.as_view(), name='index'),
 path('colecciones/', ColeccionList.as_view(), name='coleccionList'),
 path('autores/', AutorList.as_view(), name='autorList'),
 path('tags/', TagList.as_view(), name='tagList'),
 path('autor/<int:pk>/', AutorDetail.as_view(), name='autorDetail'),
 path('comic/<int:pk>/', ComicDetail.as_view(), name='comicDetail'),
 path('coleccion/<int:pk>/', ColeccionDetail.as_view(), name='coleccionDetail'),
 path('comic/<int:pk>/numeroPaginahelp', PageView.as_view(), name='pageView'),
 path('prueba/', Prueba.as_view(), name='baseIndividual'),
]