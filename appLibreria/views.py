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

class AutorDetail(DetailView):
	template_name = 'autorDetail.html'
	model = Autor


class ComicDetail(DetailView):
	template_name = 'comicDetail.html'
	model = Comic


class ColeccionDetail(DetailView):
	template_name = 'coleccionDetail.html'
	model = Coleccion


class PageView(DetailView):
	template_name = 'pageView.html'
	model = Comic
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_ = self.kwargs.get("page")
		pk_ = self.kwargs.get("pk")
		subcategory = Comic.objects.get(pk=pk_)
		context = {
			'comic' :subcategory.nombreComic,
			'num_pag' :subcategory.numPaginas,
			'objecto_comic' : subcategory,
			'pagina' :page_
		}
		return context