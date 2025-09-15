"""
项目url管理文件
URL configuration for django_keshihua project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("admin/", admin.site.urls),
    path('', include('apps.index.urls')),  # 这里是添加应用路由配置
    path('amoyjob/', include('apps.Amoyjob.urls')),  # 厦门招聘数据应用
    path('', include('apps.login.urls')),  # 登录页面
    path('', include("apps.web_fengmian.urls")),  # 首页封面
    path('', include("apps.Data_Center.urls")),  # 数据中心
    path('', include("apps.trmall_order_resport.urls")),  # 天猫销售数据
    path('silk/', include('silk.urls', namespace='silk')),  # 数据监控
]
