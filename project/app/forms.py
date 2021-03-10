from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    mail = forms.EmailField(label='Your mail', max_length=100)
    message = forms.CharField(label='Your message', max_length=500)