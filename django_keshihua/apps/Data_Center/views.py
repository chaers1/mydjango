from django.shortcuts import render
from apps.Data_Center import Amoyjob, models


# 数据中心应用

# Create your views here.
def datacenter(request):
    pandas_data_frame = ''
    username = request.session.get('username')
    if request.method == "POST":
        button_cender = request.POST.get('data_option', '没有接收到前端信号请检查')
        pandas_data_frame = Amoyjob.amoy_job_def(getattr(models, button_cender)).to_html()

    return render(request, 'datacenter.html', {'username': username, 'pandas_data_frame': pandas_data_frame})
