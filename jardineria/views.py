from django.shortcuts import render, redirect
from .models import Jardineria
from .forms import JardineriaForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def Principal1(request):
    return render(request, "Principal1.html")

def segundo(request):
    return render(request, "segundo.html")

def tercero(request):
    return render(request, "tercero.html")

def Formulario(request):
    return render(request, "formulario.html")

def Decertico(request):
    return render(request, "decertico.html")

def terminosycondiciones(request):
    return render(request, "terminosycondiciones.html")

def crear(request):
    if request.method == "POST":
        form = JardineriaForm(request.POST, request.FILES)
        if JardineriaForm.is_valid():
            JardineriaForm.save()
            return redirect('otro')
    else:
        JardineriaForm = JardineriaForm()
        print(form)
    return render(request, 'crear.html', {'JardineriaForm': JardineriaForm})

def base(request):
    return render(request, "base.html")

def otra(request):
    Jardineria= Jardineria.objects.all()
    datos={
        'jardinerias':Jardineria
    }
    return render(request, 'otro.html', datos)



def mostrar(request):
    jardinerias = Jardineria.objects.all()
    datos={
        'jardinerias':Jardineria
    }
    return render(request,'mostrar.html',datos)   

def crear(request):
    if request.method=="POST":
        JardineriaForm = JardineriaForm(request.POST) 
        if JardineriaForm.is_valid():
            JardineriaForm.save()
            return redirect('main')
    else:
        JardineriaForm=JardineriaForm()
    return render(request, 'crear.html', {'JardineriaForm':JardineriaForm})

@login_required
def eliminar(request, id):
    plantaEliminada =   Jardineria.objects.get(codigo=id)
    plantaEliminada.delete()
    return redirect ('otro')

@login_required
def modificar(request, id):
    Jardineria = Jardineria.objects.get(codigo=id)
    datos = {
        'form': JardineriaForm(instance=Jardineria)
    }
    if request.method=='POST':
        formulario = JardineriaForm(data=request.POST, instance=Jardineria)
        if formulario.is_valid():
            formulario.save()
            return redirect('otro')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('main')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)


