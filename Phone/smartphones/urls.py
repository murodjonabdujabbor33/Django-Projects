from django.urls import path
from .views import get_brands, get_models, get_products, HomaPageView

urlpatterns = [
    path('', HomaPageView.as_view(), name='home'),
    path('brand/', get_brands, name='brands'),
    path('brand/model/', get_models, name='models'),
    path('brand/model/product/', get_products, name='products'),
]