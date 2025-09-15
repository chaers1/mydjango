from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class MyAdmin(models.Model):
    '''
    用户注册登录信息ORM映射模块
    '''
    username = models.CharField(max_length=150, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=128, verbose_name='密码')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self,*args,**kwargs):
        self.set_password(self.password)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.username  # 添加冒号
