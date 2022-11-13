from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Brand, Model, Product

# Create your views here.

class HomaPageView(TemplateView):
    template_name = 'home.html'

def get_brands(request):
    queryset = Brand.objects.all()
    # print(queryset)
    return render(request, 'brands-table.html', {'brand_names': queryset})

def get_models(request):
    queryset = Model.objects.all()
    # print(queryset)
    return render(request, 'models-table.html', {'model_names': queryset})

def get_products(request, model):
    queryset = Product.objectsfilter(title__istartswith='R').all()
    # print(queryset)
    return render(request, 'products-table.html', {'product_names': queryset})
