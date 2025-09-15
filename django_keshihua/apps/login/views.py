from django.shortcuts import render, redirect,reverse
from .models import MyAdmin
import pdb


# Create your views here.

def login(request):
    '''登录视图函数'''
    if request.method == 'POST':
        button_value = request.POST.get('login', None)#这里出现一个none是用于一个指定的值
        if button_value == 'login':
            username = request.POST.get('login_name')
            password = request.POST.get('login_password')
            if username and password:  # 确保用户名和密码都不为空
                try:

                    mysql_name = MyAdmin.objects.get(username=username)
                except MyAdmin.DoesNotExist:
                    return render(request, 'login.html', {'error_message': '用户名不存在'})

                if mysql_name.check_password(raw_password=password):
                    request.session['username'] = username
                    return redirect('index')  # 登录成功后重定向到首页
                else:
                    return render(request, 'login.html', {'error_message': '密码不正确'})

            else:
                return render(request, 'login.html', {'error_message': '用户名和密码不能为空'})

    return render(request, "login.html")


def register(request):
    '''注册视图函数'''
    if request.method == 'POST':
        name = request.POST.get('username')  # 获取注册表单中的用户名
        if name:  # 检查用户名是否为空
            password = request.POST.get('password')  # 获取用户注册密码
            MyAdmin.objects.create(username=name, password=password)  # 将要注册信息添加到数据库中
            return redirect('login_sucess')  # 定向到注册成功界面
        else:
            # 如果用户名为空，返回注册页面并显示错误消息
            return render(request, 'register.html', {'error_message': '用户名不能为空'})

    else:
        return render(request, 'register.html')


def login_sucess(request):
    return render(request, 'login_sucess.html')
