from django.db import models

# Create your models here.
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