from django.shortcuts import render,redirect
from .models import Libro,Editorial,Autor
from .forms import LibroForm,EditorialForm,AutorForm

# Create your views here.

def listar_libro(request):
    libro = Libro.objects.all()
    return render(request, "lista_libros.html", {'Largo':libro})

def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('Lista_libro')
            except:
                pass
    else:
        form = LibroForm()
    return render(request, 'crear_libros.html', {'form': form})

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('Lista_libro')
    return render(request,'editar_libros.html',{'form':form})

def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('Lista_libro')