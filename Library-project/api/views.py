from django.shortcuts import render
from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializers # modeldagi ma'lumotlarni json ga o'tkazish

# Create your views here.

class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers