# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from . models import Products
from . forms import Add_stock, Sub_stock


def stock_available(request):
    products = Products.objects.all()
    context = {'Products': products}
    return render(request, 'stock.html', context)


def Purchase(request, id):
    details = Products.objects.get(id=id)
    form = Add_stock(request.POST, instance=details)
    if form.is_valid():
        values = form.save(commit=False)
        values.quantity += values.purchased
        values.save()
        return redirect('stock')
    context = {'Details': details}
    return render(request, 'add_stock.html', context)


def Sale(request, id):
    details = Products.objects.get(id=id)
    form = Sub_stock(request.POST, instance=details)
    if form.is_valid():
        values = form.save(commit=False)
        values.quantity -= values.sold
        values.save()
        return redirect('stock')
    context = {'Details': details}
    return render(request, 'sub_stock.html', context)
