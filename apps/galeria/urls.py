from django.urls import path
from apps.galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem', imagem, name='imagem'),
]