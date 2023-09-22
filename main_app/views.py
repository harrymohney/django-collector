from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

finches = [
    {'name': 'Canary Finch', 'color': 'Yellow', 'size': 'Small'},
    {'name': 'Bengalese Finch', 'color': 'Brown', 'size': 'Small'},
    {'name': 'Diamond Firetail Finch', 'color': 'Multicolored', 'size': 'Small'},
    {'name': 'Owl Finch', 'color': 'White and Gray', 'size': 'Small'},
    {'name': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', 
    { 
        'finches': finches
    }
)

def finch_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    template_name = 'finches/finch_form.html'

class FinchUpdate(UpdateView):
    model = Finch
    template_name = 'finches/finch_form.html'
    fields = ['name', 'color', 'size']

class FinchDelete(DeleteView):
    model = Finch
    template_name = 'finches/confirm_delete.html'
    success_url = '/finches/'