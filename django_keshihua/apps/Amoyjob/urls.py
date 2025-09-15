from apps.Amoyjob import views
from django.urls import path

urlpatterns = [

        path('', views.amoyjob, name='amoyjob')
]