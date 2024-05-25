from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name ='index'), # rota principal
    path('imagem/', imagem, name='imagem')
]