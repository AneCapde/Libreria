from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from  .models import Autor, Coleccion, Comic, Tag

class Index(ListView):
	template_name = 'index.html'
	model = Comic
		 
class ColeccionList(ListView):
	template_name = 'coleccionList.html'
	model = Coleccion

class AutorList(ListView):
	template_name = 'autorList.html'
	model = Autor

class TagList(ListView):
	template_name = 'tagList.html'
	model = Tag

	# def get_context_data(self, **kwargs):
	# 	# Cargar el contexto base
	# 	context = super().get_context_data(**kwargs)
	# 	# Añadir un listado de departamentos
	# 	context['coleccion_list'] = Coleccion.Tag.all()
	# 	context['autor_list'] = Coleccion.Autor.all()
	# 	return context

class AutorDetail(DetailView):
	template_name = 'autorDetail.html'

	model = Autor

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
 		context = super().get_context_data(**kwargs)
 		context['coleccion_list'] = Coleccion.objects.all()
 		return context

class ComicDetail(DetailView):
	template_name = 'comicDetail.html'

	model = Comic

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		context['coleccion_list'] = Coleccion.objects.all()
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context

class ColeccionDetail(DetailView):
	template_name = 'coleccionDetail.html'

	model = Coleccion

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		# Añadir un listado de departamentos
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context

class PageView(DetailView):
	template_name = 'pageView.html'

	model = Comic

	def get_context_data(self, **kwargs):
		# Cargar el contexto base
		context = super().get_context_data(**kwargs)
		context['autor_list'] = Autor.objects.all()
		context['tag_list'] = Tag.objects.all()
		return context

class Prueba(ListView):
	template_name = 'baseIndividual.html'

	model = Comic