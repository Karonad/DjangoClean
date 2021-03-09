from django.shortcuts import render
from .models import Fruits
# Create your views here.
def index(request):
    test = 'wesh'
    fruits = Fruits.objects.all()
    return render(request, 'app/index.html', {'fruits': fruits})
