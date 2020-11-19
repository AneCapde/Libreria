from django.urls import path
from appLibreria.views import Index

urlpatterns = [
 path('', Index.as_view(), name='index'),
]