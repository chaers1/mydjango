'''
这里是一个数据库原型，通过这里进行数据获取和pandas数据转换
'''
import pandas as pd


def amoy_job_def(models_class):
    '''
    models_class : 传入models中的数据模型
    '''
    filterde_data = models_class.objects.all().values()[:50]
    data_list = list(filterde_data)
    df = pd.DataFrame(data_list)
    return df
