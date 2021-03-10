from django.conf.urls import url
from django.urls import path

from . import views # import views so we can use them in urls.


urlpatterns = [
    path('', views.index), # "/store" will call the method "index" in "views.py"
    path('contact/', views.contact), # "/store" will call the method "index" in "views.py"
]