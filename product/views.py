from django.shortcuts import render

from .models import *


def product_list(request):
	q = request.GET.get('q')
	if q:
		products = Product.objects.filter(title__icontains=q)	
	else:
		products = Product.objects.all()

	return render(request, 'product_list.html', {
		'products': products
	})	


def product_detail(request, id):
	product = Product.objects.get(id=id)

	return render(request, 'product_detail.html', {
		'product': product
	})
