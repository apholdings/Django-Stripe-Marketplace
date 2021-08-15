from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from marketplace.models import Product


class HomeView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(active=True)

        if products:
            paginator = Paginator(products, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'products':digital_products_data
        }
        return render(request, 'pages/index.html', context)