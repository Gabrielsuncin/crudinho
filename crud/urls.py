from django.urls import path
from .views import index, visualiza_produtos, cria_produtos

urlpatterns = [
    path('', index, name='index'),
    path('visualiza/', visualiza_produtos, name='visualiza'),
    path('criar/', cria_produtos, name='cria_produtos')
]