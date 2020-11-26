from django.http import HttpResponse
from django.views.generic import TemplateView, ListView#, DetailView, TemplateView
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

# class Coleccion(DetailView):
# 	template_name = 'coleccion.html'
# 	queryset = get_list_or_404(Coleccion.objects.all())

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	id_ = self.kwargs.get("pk")
	# 	coleccion = Coleccion.objects.get(pk=id_)
	# 	context['tags_coleccion'] =  coleccion.Tags.all()
	# 	context['autores_coleccion'] =  coleccion.Autors.all()
	# 	return context
