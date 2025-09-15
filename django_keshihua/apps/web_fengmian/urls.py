from apps.web_fengmian import views
from django.urls import path

urlpatterns = [
    path('', views.wen_fengmian, name='web_fengmian')
]