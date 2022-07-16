from multiprocessing import context
from django.shortcuts import render

from site_institucional.models import Inicio
from site_institucional.models import QuemSomos
from site_institucional.models import Servicos
from site_institucional.models import Portfolio
from site_institucional.models import Contato
from site_institucional.models import Formulario

# Create your views here.
def home(request):
    inicio = Inicio.objects.last()
    quemsomos = QuemSomos.objects.last()
    servicos = Servicos.objects.last()
    portfolio = Portfolio.objects.last()
    contato = Contato.objects.last()


    context = {
        'inicio': inicio,
        'quemsomos': quemsomos,
        'servicos': servicos,
        'portfolio': portfolio,
        'contato': contato
        
    }
    
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']
        mensagem = request.POST['mensagem']

        form = Formulario(nome=nome, email=email, whatsapp=whatsapp, mensagem=mensagem)
        form.save()
        
    return render(request, 'index.html', context)