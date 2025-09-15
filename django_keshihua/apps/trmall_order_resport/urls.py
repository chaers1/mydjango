from django.urls import path
from apps.trmall_order_resport import views

urlpatterns = [

    path('tianmao', views.tianmao, name='tianmao')
]
