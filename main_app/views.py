from django.shortcuts import render
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

# def index(request):
#     finches = Finch.objects.all()
#     context = {'finches': finches}
#     return render(request, 'finches/index.html', context)

def finches_index(request):
    return render(request, 'finches_index.html')