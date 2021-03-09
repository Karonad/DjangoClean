from django.shortcuts import render
from .models import Fruits
# Create your views here.
def index(request):
    test = 'wesh'
    # fruits = Fruits.objects.filter()
    return render(request, 'app/index.html', {'test': fruits})
