from celery import shared_task
from .models import Amoyjob
from celery.result import AsyncResult


@shared_task
def mysql_object(colums: list):
    try:
        filter_object = Amoyjob.objects.all().values(*colums)
        result = list(filter_object)
        print(f"Query completed. Found {len(result)} records with columns: {colums}")
        return result if result else []

    except Exception as e:
        print(f'Error in mysql_object task: {e}')
        return []


@shared_task
def execute_async_tasks(lists: list):
    '''
    执行异步数据库查询任务
    list : 数据库查询条件
    '''
    try:
        # 直接调用查询函数而不是创建另一个任务
        result = mysql_object(lists)
        return result if result is not None else []
    except Exception as e:
        print(f"Error in execute_async_tasks: {e}")
        return []
