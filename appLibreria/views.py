from django.http import HttpResponse
from django.views.generic import ListView, DeleteView
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
		subcategory = Coleccion.objects.get(pk=id_)
		context['lista_rutas'] =  Coleccion.objects.filter(pais = pais_)
		context['lista_hotel'] =  Hotel.objects.filter(pais = pais_)
		return context
