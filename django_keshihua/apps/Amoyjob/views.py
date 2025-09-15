from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .pandas_pyecharts import pyecharts_zhengti, pyecharts_hangye, pyecharts_gongsi, pyecharts_position_max, \
    pyecharts_map_xiamen, title_jineng
from celery.result import AsyncResult


# Create your views here.

@cache_page(60 * 15)
def amoyjob(request):
    username = request.session.get('username')

    colums = {'username': username}
    dump_dict = {'page_dump_one_bai': pyecharts_zhengti(), 'page_dump_tow_bar': pyecharts_hangye(),
                 'page_dump_tree_pei': pyecharts_gongsi(), 'page_dump_foor_funnel': pyecharts_position_max(),
                 'page_dump_file_map': pyecharts_map_xiamen(), 'title_dict': title_jineng()}
    colums.update(dump_dict)

    return render(request, 'amoyjob.html', colums)
