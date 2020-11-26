from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from  .models import Autor, Coleccion, Comic, Tag

class Index(ListView):
	template_name = 'index.html'
	#Portada, titulo, a que coleccion pertenece, tags y autor x10
	#en la barra lateral poner recomendaciones (al azar)
	#queryset = get_list_or_404(Coleccion.objects.all())
	model = Comic

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
 		context = super().get_context_data(**kwargs)
 		# Añadir un listado de departamentos
 		context['coleccion_list'] = Coleccion.objects.all()
 		return context
		 
class ColeccionList(DetailView):
	template_name = 'coleccionList.html'
	queryset = get_list_or_404(Coleccion.objects.all())

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		id_ = self.kwargs.get("pk")
		coleccion = Coleccion.objects.get(pk=id_)
		context['tags_coleccion'] =  coleccion.Tags.all()
		context['autores_coleccion'] =  coleccion.Autors.all()
		return context

class AutorList(ListView):
	template_name = 'autorList.html'

	model = Autor

class TagList(ListView):
	template_name = 'tagList.html'

	model = Tag

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		# Añadir un listado de departamentos
		context['coleccion_list'] = Coleccion.Tag.all()
		context['autor_list'] = Coleccion.Autor.all()
		return context

class AutorDetail(ListView):
	template_name = 'autorDetail.html'

	model = Autor

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
 		context = super().get_context_data(**kwargs)
 		# Añadir un listado de departamentos
 		context['coleccion_list'] = Coleccion.objects.all()
 		return context

class ComicDetail(ListView):
	template_name = 'comicDetail.html'

	model = Comic

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		# Añadir un listado de departamentos
		context['coleccion_list'] = Coleccion.objects.all()
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context

class ColeccionDetail(ListView):
	template_name = 'coleccionDetail.html'

	model = Coleccion

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		# Añadir un listado de departamentos
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context

class PageView(ListView):
	template_name = 'pageView.html'

	model = Comic

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		# Añadir un listado de departamentos
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context