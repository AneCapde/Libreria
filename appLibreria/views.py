from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from  .models import Autor, Coleccion,  Comic, Tag

class Index(ListView):
	template_name = 'index.html'
	queryset = get_list_or_404(Coleccion.objects.all())

class Coleccion(DetailView):
	template_name = 'coleccion.html'
	queryset = get_list_or_404(Coleccion.objects.all())

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		id_ = self.kwargs.get("pk")
		coleccion = Coleccion.objects.get(pk=id_)
		context['tags_coleccion'] =  coleccion.Tags.all()
		context['autores_coleccion'] =  coleccion.Autors.all()
		return context
