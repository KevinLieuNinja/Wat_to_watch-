from django.shortcuts import render, redirect
from Show_app.models import *
# Create your views here.

from django.contrib import messages


def index(request):
    context={
        'Shows' : Show.objects.all()
    }
    return render(request, 'Main.html', context)

def view_show(request, id):
    context={
        'show' : Show.objects.get(id=id)
    }
    return render(request, 'views.html', context)

def edit_show(request, id):
    Shows = Show.objects.get(id=id)
    context={
        'show' : Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def update_show(request, id):

    errors= Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, value in errors.items():
            messages.error(request, value)
        return redirect('/edit_show/'+ str(id))

    if request.POST:
        shows = Show.objects.get(id=id)
        shows.title = request.POST['title']
        shows.network = request.POST['network']
        shows.release_date = request.POST['release_date']
        shows.description = request.POST['description']
        shows.save()
        return redirect('/view_show/'+ str(id))


def add_show(request):    
    return render(request, 'new.html')

def create_show(request):
    errors= Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, value in errors.items():
            messages.error(request, value)
        return redirect('/add_show')

    else:
        Nunu = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        return redirect('/view_show/'+str(Nunu.id))


def delete_show(request, id):
    Shows = Show.objects.get(id=id)
    Shows.delete()
    return redirect('/')