from django.db import models


# Create your models here.

class Amoyjob(models.Model):
    id = models.BigIntegerField(primary_key=True, blank=True, null=False)
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
