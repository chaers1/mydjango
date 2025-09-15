from django.urls import path
from apps.login import views

urlpatterns = [
    path('login/', views.login, name='login'),  # 登录页面
    path('register/', views.register, name='register'),  # 注册页面
    path('login_sucess/', views.login_sucess, name='login_sucess')
]