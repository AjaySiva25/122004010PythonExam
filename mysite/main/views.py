from django.shortcuts import render
from .models import Bus, Busform
from django.http import HttpResponseRedirect
def index(request):
    return render(request, 'index.html')

def display(request):
    bus = Bus.objects.all()
    return render(request, 'display.html', {'bus':bus})

def Busdeets(request):
    bus = Bus.objects.all()
    c = dict({'bus':bus, 'form':Busform()})
    return render(request, 'details.html', c)

def create_deets(request):
    if request.method=='POST':
        form = Busform(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('/')

def search(request):
    num = request.POST['bno']
    det = Bus.objects.get(bno=num)
    return render(request,'search.html', {'det':det})





