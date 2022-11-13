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

def get_models(request, model_name):
    queryset = Model.objects.all().filter(model=model_name)
    # print(queryset)
    return render(request, 'models-table.html', {'model_names': queryset})

def get_products(request, brand_name):
    queryset = Product.objects.all().filter(model=brand_name)
    brand = Model.objects.get(model=brand_name)
    context = {'products':queryset, 'brand':brand}
    return render(request, 'products-table.html', context)
