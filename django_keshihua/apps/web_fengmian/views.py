from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.urls import reverse


def wen_fengmian(request):
    template = loader.get_template("new_file.html")
    if request.method == 'POST':
        login_url = reverse('login')  # 获取登录页面的URL
        return redirect(login_url)  # 重定向到登录页面

    else:
        return HttpResponse(template.render({}, request))
