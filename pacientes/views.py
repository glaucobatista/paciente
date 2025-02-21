from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
from .models import Pacientes

def pacientes(request):
    
    if request.method == "GET":
        pacientes = Pacientes.objects.all()
        return render(request, 'pacientes.html', {'queixas':Pacientes.queixa_choices, 'pacientes':pacientes})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        # foto = request.POST.get('foto')
        foto = request.FILES.get('foto')

        print(nome,email,telefone,queixa,foto)
        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return render(request, 'pacientes.html', {'queixas':Pacientes.queixa_choices})
        
        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto,
        )
        paciente.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')

        return render(request, 'pacientes.html', {'queixas':Pacientes.queixa_choices})
