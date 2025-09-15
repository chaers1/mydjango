from apps.Data_Center import views
from django.urls import path

urlpatterns = [

    path('datacenter/', views.datacenter, name='datacenter'),

]
