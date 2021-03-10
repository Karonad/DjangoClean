from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Fruits, Contact
from app.forms import ContactForm
import datetime
# Create your views here.
def index(request):
    test = 'wesh'
    fruits = Fruits.objects.all()
    return render(request, 'app/index.html', {'fruits': fruits})


def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                mail = form.cleaned_data['mail'],
                name = form.cleaned_data['name'],
                message = form.cleaned_data['message'],
                # created_at = date.today(),
                # updated_at = datetime.datetime.now()
                
           )    
            form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})

