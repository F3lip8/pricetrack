from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
from .models import Produto



def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            produto.adicionar_produto()
            return redirect('index.html')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

def atualizar_produto():
    produtos = Produto.objects.all()
    for produto in produtos:
        produto.atualizar_dados()
        resultado = produto.atualizar_dados()
        if resultado:
            print(f"Preço atualizado: R${resultado['preco']} - {resultado['titulo']}")
    return redirect('index.html')
