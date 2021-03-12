from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index), 
    path('contact/', views.contact), 
    path('cv/', views.cv), 
    path('cv/<int:id>/', views.cv_show), 
    path('cv/ajout/', views.cv_ajout), 
]