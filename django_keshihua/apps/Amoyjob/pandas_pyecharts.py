'''
利用异步执行完的结果进行数据分析和可视化准备
'''

from .tasks import execute_async_tasks
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Funnel, Map
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from collections import Counter
import re

##############################################常量设定 远程主机 ###########################################
REMOTE_HOST = "https://pyecharts.github.io/assets/js"  # 定义远程主机

#明天更改代码，在异步中编写框架，然后通过调用来完成异步的数据查询和处理
#################################################数据分析以及绘图#########################################################
def pyecharts_zhengti():
    '''
    针对整体数据进行分析，（招聘企业数（company，岗位数（position）,职位分类数量（），招聘人数（num），平均工资（salary））
    :param df: 数据集
    :return: bar绘图图例
    '''
    lists = ['company', 'position', 'num', 'salary']
    result = execute_async_tasks(lists=lists)
    df_conums = pd.DataFrame(result)
    df_conums['num'] = pd.to_numeric(df_conums['num'], errors='coerce')
    company_counts = len(df_conums['company'].value_counts())  # 招聘企业总数
    position_sum = len(df_conums['position'].value_counts())  # 职位分类数量
    position_count = int(df_conums['position'].count())
    num_sum = df_conums['num'].sum()  # 招聘总人数
    df_conums['salary'] = df_conums['salary'].str.replace(r'\D', '', regex=True)
    df_conums['salary'] = pd.to_numeric(df_conums['salary'], errors='coerce')
    salary_average = df_conums['salary'].mean().round(2)

    df_dict = {'招聘企业总数': company_counts, '岗位总数数': position_count, '岗位分类数量': position_sum, '总招聘人数': num_sum,
               '平均工资': salary_average}

    bar = (

        Bar(init_opts=opts.InitOpts(
            width='530px',
            height='400px',
            theme=ThemeType.CHALK,
            animation_opts=opts.AnimationOpts(animation=1000, animation_duration=1000),
            chart_id='scatter1'
        ))

            .add_xaxis(list(df_dict.keys()))
            .add_yaxis('招聘预览', list(df_dict.values()), bar_width='40%')
            .set_global_opts(
            title_opts=opts.TitleOpts(title='厦门整体招聘人数概览'),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=40))
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""
                    ),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "rgb(0, 160, 221)",
                }
            }

        )
    )
    context = dict(
        myechart=bar.render_embed(),
        host=REMOTE_HOST,
    )
    # print(context)
    return context


def pyecharts_hangye():
    '''
    厦门招聘数据行业情况分析，使用 industry列和 num 中的数据进行对比
    主要是公司所属行业继续宁招聘数量的统计
    :param df:数据源
    :return: bar
    '''
    lists = ['industry', 'num']
    result = execute_async_tasks(lists=lists)
    df_industry_num = pd.DataFrame(result)
    df_industry_num['num'] = pd.to_numeric(df_industry_num['num'], errors='coerce')
    df_groupby = df_industry_num.groupby('industry')['num'].sum().nlargest(10)
    bar = (
        Bar(init_opts=opts.InitOpts(width='530px', height='400px',
                                    theme=ThemeType.ESSOS,
                                    animation_opts=opts.AnimationOpts(animation_delay=1000, animation_duration=1000),
                                    chart_id='scatter6',
                                    ))
            .add_xaxis(df_groupby.index.tolist())
            .add_yaxis('招聘数据', df_groupby.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title='各行业招聘数据排行TOP10'),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=40))
        )
    )

    context = dict(
        myechart=bar.render_embed(),
        host=REMOTE_HOST,
    )
    # print(context)
    return context


def pyecharts_gongsi():
    lists = ['company_type', 'num']
    result = execute_async_tasks(lists=lists)
    df_company_type_num = pd.DataFrame(result)
    df_company_type_num['num'] = pd.to_numeric(df_company_type_num['num'])
    df_company_num_groupby = df_company_type_num.groupby('company_type')['num'].sum()
    df_pair = [i for i in zip(df_company_num_groupby.index.tolist(), df_company_num_groupby.tolist())]
    df_pair.sort(key=lambda x: x[1])

    pie = (
        # 初始化 Pie 图表，设置背景颜色
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c",
                                    chart_id='scatter5',
                                    width='530px',
                                    height='400px',
                                    ))

            # 添加数据和选项
            .add(
            # 设置饼图的内外半径
            radius=["40%", "55%"],
            # 设置系列名称
            series_name="招聘人数",
            # 设置数据对，即 (名称, 数值) 对列表
            data_pair=df_pair,
            # 设置标签选项
            label_opts=opts.LabelOpts(
                # 设置标签位置为外部
                position="outside",
                # 设置标签的格式化字符串
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                # 设置标签的背景颜色
                background_color="#eee",
                # 设置标签的边框颜色
                border_color="#aaa",
                # 设置标签的边框宽度
                border_width=0,
                # 设置标签的边框圆角
                border_radius=6,
                # 设置标签中富文本的样式
                rich={
                    "a": {"color": "#999", "lineHeight": 35, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            )
        )
            # 设置全局选项
            .set_global_opts(
            # 设置标题选项
            title_opts=opts.TitleOpts(
                title='各类型公司招聘人数',
                title_textstyle_opts=opts.TextStyleOpts(color='#fff'),
            ),
            # 设置图例选项
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    context = dict(
        myechart=pie.render_embed(),
        host=REMOTE_HOST,
    )
    # print(context)
    return context


def pyecharts_position_max():
    '''
    #最确认的公司可以从每一个公司招聘的人数来官产主要使用 position（公司名字）和num（招聘人数）
    :param df: 数据源
    :return: Funnel
    '''
    lists = ['company', 'num']
    result = execute_async_tasks(lists=lists)
    df_company_num = pd.DataFrame(result)
    df_company_num['num'] = pd.to_numeric(df_company_num['num'])
    df_company_num_groupby = df_company_num.groupby('company')['num'].sum().nlargest(10)
    top_ten_typles = [(index, value) for index, value in df_company_num_groupby.items()]
    funnel = (
        Funnel(init_opts=opts.InitOpts(chart_id='scatter3',
                                       width='650px',
                                       height='400px',
                                       ))
            .add('岗位数', top_ten_typles)
            .set_global_opts(title_opts=opts.TitleOpts(title='公司招聘岗位数TOP10'),
                             legend_opts=opts.LegendOpts(is_show=False))
    )
    context = dict(
        myechart=funnel.render_embed(),
        host=REMOTE_HOST,
    )
    # print(context)
    return context


def pyecharts_map_xiamen():
    '''
    厦门地理信息 workplace 主要是用 workplace 来绘制地区地图，岗位数量的分布图，颜色越深代表数量越大，
    可以看到思明区的工作机会最多，其次是湖里、集美、同安、海沧、翔安。
    :param df: 数据源
    :return: mapp
    '''
    lists = ['workplace']
    result = execute_async_tasks(lists=lists)
    df = pd.DataFrame(result)
    xiamen_data = df[df['workplace'].str.contains('厦门市', na=False)]
    xiamen_workplace = xiamen_data['workplace'].str.split('、').explode()  # 直接在 xiamen_data 上进行操作
    xiamen_workplace = xiamen_workplace[xiamen_workplace.str.contains('厦门市', na=False)]
    data_workplace = Counter(xiamen_workplace)

    pattern = re.compile(r'厦门市(.*?区)')

    porcets_dict = {}

    for key, value in data_workplace.items():
        match = pattern.search(key)
        if match:
            district = match.group(1)
            porcets_dict[district] = value

    porcets_list = [[key, value] for key, value in porcets_dict.items()]

    mapp = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.CHALK,
                                    chart_id='scatter2',
                                    width='650px',
                                    height='400px',
                                    ))
            .add('地区', data_pair=porcets_list[:-3], maptype='厦门')
            .set_global_opts(title_opts=opts.TitleOpts(title='厦门招聘分布'))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter='{b} : {c}'))
    )

    context = dict(
        myechart=mapp.render_embed(),
        host=REMOTE_HOST,
    )
    # print(context)
    return context


def title_jineng():
    '''
    it个岗位需求
    '''
    lists = ['industry', 'salary', 'skill']
    result = execute_async_tasks(lists=lists)
    df = pd.DataFrame(result)
    df_num_skill = df[df['industry'] == 'IT互联网']
    df_num_skill_expanded = df_num_skill.assign(skill=df_num_skill['skill'].str.split('、')).explode('skill')
    skills_to_filter = ['python', 'JAVA', 'C++', 'JavaScript', 'Ruby', 'C', 'Go', 'PHP']
    df_num_skill = df_num_skill_expanded[df_num_skill_expanded['skill'].isin(skills_to_filter)].dropna(subset='salary')
    df_num_skill['salary'] = pd.to_numeric(df_num_skill['salary'], errors='coerce').fillna(0).astype(int)
    set_dict = dict()
    df_num_skill = df_num_skill.groupby('skill')
    for skill, group_data in df_num_skill:
        set_dict[skill] = {
            '招聘岗位': int(group_data['skill'].count()),
            '平均工资': float(round(group_data['salary'].mean(), 2))
        }
    return set_dict


###################################数据分析和可视化任务启动模式############################################
# 运行数据分析和可视化任务
# def run_redder_embed():
#     # 创建任务结果字典
#     dicts = {}
#
#     # 任务列表
#     tasks = [
#         pyecharts_zhengti,
#         pyecharts_hangye,
#         pyecharts_gongsi,
#         pyecharts_position_max,
#         pyecharts_map_xiamen,
#         title_jineng,
#     ]
#
#     # 获取 CPU 核心数，确定启动几个进程来执行任务
#     num_processes = multiprocessing.cpu_count()
#     prtcesses = 0
#
#     if num_processes == 4:
#         prtcesses = 1
#     elif num_processes <= 8:
#         prtcesses = 2
#     else:
#         prtcesses = 2
#
#     # 创建进程池
#     with multiprocessing.Pool(processes=prtcesses) as pool:
#         # 并行执行任务列表中的每个任务
#         try:
#             # 尝试执行任务并获取结果
#             results = [pool.apply_async(run_task, args=(task_func,)) for task_func in tasks]
#
#             # 等待所有任务完成
#             for key_dump, result in zip(TASK_KEY_LIST, results):
#                 success, task_result = result.get()  # 获取多进程执行结果
#                 print(task_result)
#
#                 if success:
#                     dicts[key_dump] = task_result
#         except Exception as e:
#             # 捕获所有类型的异常并打印错误信息
#             print(f"An error occurred: {e}")
#
#     return dicts
#
#
# # 定义一个函数，用于执行每个任务
# def run_task(task_func):
#     try:
#         result = task_func()
#         return True, result
#     except Exception as e:
#         return False, e
