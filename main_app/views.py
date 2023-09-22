from django.shortcuts import render
from .models import Finch

finches = [
    {'name': 'Canary Finch', 'color': 'Yellow', 'size': 'Small'},
    {'name': 'Bengalese Finch', 'color': 'Brown', 'size': 'Small'},
    {'name': 'Diamond Firetail Finch', 'color': 'Multicolored', 'size': 'Small'},
    {'name': 'Owl Finch', 'color': 'White and Gray', 'size': 'Small'},
    {'name': 'Zebra Finch', 'color': 'Gray', 'size': 'Small'}
]

def all_finches(request):
    finches = Finch.objects.all()
    context = {'finches': finches}
    return render(request, 'all_finches.html', context)

def about(request):
    return render(request, 'about.html')