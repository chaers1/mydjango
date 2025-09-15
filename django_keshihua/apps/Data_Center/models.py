# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amoyjob(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=False, null=False)
    position = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=255, blank=True, null=True)
    jobage = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    age = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    workplace = models.CharField(max_length=255, blank=True, null=True)
    worktime = models.CharField(max_length=255, blank=True, null=True)
    salary = models.CharField(max_length=255, blank=True, null=True)
    welfare = models.CharField(max_length=255, blank=True, null=True)
    hr = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    require = models.TextField(blank=True, null=True)
    worktime_day = models.CharField(max_length=255, blank=True, null=True)
    worktime_week = models.TextField(blank=True, null=True)
    skill = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amoyjob'

class TmallOrderReport(models.Model):
    '''
    天猫用户实际支付数据模型
    '''
    order_id = models.IntegerField(blank=True, null=True, verbose_name='订单编号',db_column='订单编号')
    total_amount = models.FloatField(blank=True, null=True, verbose_name='总金额',db_column='总金额')
    buyer_actual_payment = models.FloatField(blank=True, null=True, verbose_name='买家实际支付金额',db_column='买家实际支付金额')
    shipping_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='收货地址',db_column='收货地址')
    order_created_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单创建时间',db_column='订单创建时间')
    order_paid_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='订单付款时间',db_column='订单付款时间')
    refund_amount = models.FloatField(blank=True, null=True, verbose_name='退款金额',db_column='退款金额')

    class Meta:
        managed = False
        db_table = 'tmall_order_report'

class Sztcard(models.Model):
    '''
    深圳地铁交通数据模型
    '''
    card_no = models.CharField(max_length=255, blank=True, null=True)
    deal_date = models.CharField(max_length=255, blank=True, null=True)
    deal_type = models.CharField(max_length=255, blank=True, null=True)
    deal_money = models.CharField(max_length=255, blank=True, null=True)
    deal_value = models.CharField(max_length=255, blank=True, null=True)
    equ_no = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    station = models.CharField(max_length=255, blank=True, null=True)
    car_no = models.CharField(max_length=255, blank=True, null=True)
    conn_mark = models.CharField(max_length=255, blank=True, null=True)
    close_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SZTcard'
