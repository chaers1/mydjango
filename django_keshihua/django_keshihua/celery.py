import os
from celery import Celery

# 1 导入django的配置文件---》后续在celery的任务中，就可以直接使用django的orm，缓存。。。

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_keshihua.settings')

app = Celery('celery_root')

# 从 Django 的设置文件中加载 Celery 配置
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_pool_limit = 10  # 设置为 1，表示不使用连接池
# 自动从所有已注册的 Django app 中加载任务
app.autodiscover_tasks()

# 启动celery异步执行

# celery -A django_keshihua worker -l info -P eventlet

#启动 flower 异步监视 命令，这个工具需要打开浏览器进行
# celery -A django_keshihua flower --port=5000 --address=127.0.0.1
