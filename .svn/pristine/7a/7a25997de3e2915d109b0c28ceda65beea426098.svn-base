#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @contact: voidqueens@hotmail.com
# @software: PyCharm
# @time: 2019/7/3 下午4:01
# @site: www.gongyanli.com
# @file: urls.py
from django.urls import path, re_path
from .views import auto, auto_add, auto_del, auto_detail, auto_cancel, auto_detailInterface
from .views import selftest,selftest_add,selftest_del,selftest_cancel,selftest_detail
urlpatterns = [
    path('auto/', auto),
    path('add/', auto_add),
    path('del/', auto_del),
    path('cancel/', auto_cancel),
    path('selftest/', selftest),
    path('selftestadd/', selftest_add),
    path('selftestdel/', selftest_del),
    path('selftestcancel/', selftest_cancel),
    re_path('detail_(?P<task_id>\d+).html/', auto_detail),
    re_path('detailInterface_(?P<task_id>\d+).html/', auto_detailInterface),
    re_path('detailst_(?P<task_id>\d+).html/', selftest_detail),
]
