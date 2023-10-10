from django.shortcuts import render, redirect
from .models import Note
from django.contrib import messages
from .forms import ModelForm

# Create your views here.

def HomePage(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'home.html', context)

def CreateNote(request):
    if request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']

        create = Note.objects.create(title=title, text=text)
        create.save()
        return redirect('home')

    return render(request, 'create.html')

def ReadNote(request, pk):
    notes = Note.objects.get(id=pk)
    context = {'notes': notes}
    return render(request, 'read.html', context)

def DeleteNote(request, pk):
    notes = Note.objects.get(id=pk)
    if request.method == "POST":
        remove = notes.delete()
        return redirect('home')
    context = {'notes': notes}
    return render(request, 'delete.html', context)

def EditNote(request, pk):
    notes = Note.objects.get(id=pk)
    form = ModelForm(instance=notes)
    if request.method == "POST":
        form = ModelForm(request.POST, instance=notes)
        if form.is_valid:
            form.save();
            return redirect('home')
    context = {'form': form}
    return render(request, 'edit.html', context)