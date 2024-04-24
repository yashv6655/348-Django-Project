from django.shortcuts import render, redirect
from item.models import Type, Item
from .forms import SignupForm
from django.db import connection
# Create your views here.
def index(req):
    items = Item.objects.filter(is_sold=False)
    types = Type.objects.all()
    return render(req, 'home/index.html', {'type': types, 'items': items})

def contact(req):
    return render(req, 'home/cont.html')

def signup(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        print(form.is_valid())

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(req, 'home/signup.html', {
        'form': form
    })