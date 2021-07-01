from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Customer
from .forms import CustomerForm


def index(request):
    return render(request, 'home.html')


def product(request):
    electric = Product.objects.all()
    return render(request, 'product.html', {'electric': electric})


def contact(request):
    form = CustomerForm()
    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html', {'form': form})