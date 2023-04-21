from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu
    serializer_class = MenuSerializer
    