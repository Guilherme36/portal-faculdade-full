from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def alunos(request):
    return render(request, 'alunos.html')

def professores(request):
    return render(request, 'professores.html')

def materias(request):
    return render(request, 'materias.html')

def turmas(request):
    return render(request, 'turmas.html')
