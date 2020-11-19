from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from  .models import Autor, Coleccion,  Comic, Tag

def index(request):
	posts = get_list_or_404(Post.objects.order_by('-fecha_creacion'))#"Listado de entradas del blog", 
	context = {'lista_posts':posts}
	return render(request, 'blog.html', context)