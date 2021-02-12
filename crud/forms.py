from .models import ProdutoIlicito
from django import forms


class ProdutoIlicitoForm(forms.ModelForm):
    class Meta:
        model = ProdutoIlicito
        fields = ['nome', 'quantidade', 'porcao', 'preco']
