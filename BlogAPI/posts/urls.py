from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detail'),
    path('', PostList.as_view(), name='home'),
]