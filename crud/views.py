from django.shortcuts import render, redirect, reverse
from .models import ProdutoIlicito
from .forms import ProdutoIlicitoForm


def index(request):
    return render(request, "pagina_principal.html")


def visualiza_produtos(request):
    produtos_do_banco = ProdutoIlicito.objects.all()
    context = {
        'produtos': produtos_do_banco
    }
    return render(request, "visualiza.html", context)


def cria_produtos(request):
    form = ProdutoIlicitoForm()
    context = {
        'form': form,
    }
    if request.POST:
        form = ProdutoIlicitoForm(request.POST)
        form.save()
        return redirect(reverse('visualiza'))
    return render(request, 'cria_produtos.html', context)
