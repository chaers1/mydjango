from apps.index import views
from django.urls import path

urlpatterns = [

    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
]
