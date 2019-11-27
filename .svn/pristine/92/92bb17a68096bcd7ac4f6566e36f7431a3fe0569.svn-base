from django.shortcuts import render
from django.urls import reverse
from user_record.models import user_record
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from user_record.views import login_checker
from .models import MonitorNotice, MonitorConfig
import json
import datetime


# Create your views here.
@login_checker
def monitor_list(request):
    if request.method == 'GET':
        notice_list = []
        monitor_item = MonitorConfig.objects.all()
        for item in monitor_item:
            # print(item.__dict__)
            monitor_item_list = MonitorNotice.objects.filter(monitor_id=item.id).order_by('-id')
            if not monitor_item_list:
                continue
            item_will_add = monitor_item_list.values()[0]  # 这一步转成了字典
            status_display = monitor_item_list[0].get_status_display()
            if item_will_add.get('status') == '0':
                status_display_label = 'label label-success'
            else:
                status_display_label = 'label label-danger'
            item_will_add.update({
                'status_display': status_display,
                'status_display_label': status_display_label,
                'monitor_from': item.title,
            })
            notice_list.append(item_will_add)
        # print(notice_list)
    else:
        notice_list = []
    return_dict = {
        'notice_list': notice_list,
    }
    return [request, 'monitor_notice/monitor_list.html', return_dict]


@login_checker
def monitor_item_detail(request, id):
    if request.method == 'GET':
        notice_name = MonitorConfig.objects.get(id=id)
        notice_history = MonitorNotice.objects.filter(monitor_id=id).order_by('-id')
        notice_list_history = []
        if notice_history:
            for item in notice_history:
                dict_add = {}
                dict_add.update({
                    'id': item.id,
                    'title': item.title,
                    'status': item.status,
                    'create_time': item.create_time,
                })
                # dict_add.update(item.__dict__())
                status_display = item.get_status_display()
                if item.status == '0':
                    status_display_label = 'label label-success'
                else:
                    status_display_label = 'label label-danger'
                dict_add.update({
                    'status_display': status_display,
                    'status_display_label': status_display_label,
                })
                notice_list_history.append(dict_add)


    elif request.method == 'POST':
        notice_list_history = []
    else:
        notice_list_history = []
    return_dict = {
        'notice_list_history': notice_list_history,
        'notice_name': notice_name,
        'monitor_id': id,
    }
    return [request, 'monitor_notice/monitor_list_history.html', return_dict]


@login_checker
def monitor_config(request):
    if request.method == 'GET':
        monitor_config = MonitorConfig.objects.all()
    elif request.method == 'POST':
        monitor_config = ''
        pass
    else:
        monitor_config = ''
        pass
    return_dict = {
        'monitor_config': monitor_config,
    }
    return [request, 'monitor_notice/monitor_list_history.html', return_dict]


@csrf_exempt
def notice_receive(request):
    if request.method == 'POST':
        try:
            params = json.loads(request.body.decode('utf8'))
        except:
            fail_dict = {
                'code': '1',
                'message': 'json analyze failed',
            }
            return JsonResponse(fail_dict)

        is_error = check_params(params)
        if is_error:
            fail_dict = {
                'code': '2',
                'message': is_error,
            }
            return JsonResponse(fail_dict)
        try:
            monitor_inserted = MonitorNotice.objects.create(**params)
        except Exception as e:
            print(e)
            fail_dict = {
                'code': '3',
                'message': 'insert failed',
            }
            return JsonResponse(fail_dict)
        success_dict = {
            'code': '0',
            'message': 'OK',
        }
        return JsonResponse(success_dict)


@csrf_exempt
def page(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf8'))
        print(params)
        draw = params.get('draw')
        start = params.get('start')
        length = params.get('length')
        monitor_id = params.get('monitor_id')
        order = params.get('order')
        columns = params.get('columns')
        data_from = int(start)
        data_to = int(start) + int(length)

        # notice_name = MonitorConfig.objects.get(id=id)
        if order:
            try:
                order_param = columns[order[0].get('column')].get('data')
                order_dir = order[0].get('dir')
                order_str_template = '{}{}'
                if order_dir == 'desc':
                    order_str = order_str_template.format('-', order_param)
                else:
                    order_str = order_str_template.format('', order_param)
                print("=============", order_str)
                notice_history = MonitorNotice.objects.filter(monitor_id=monitor_id).order_by(order_str)
            except Exception as e:
                print(e)
                notice_history = MonitorNotice.objects.filter(monitor_id=monitor_id).order_by('-id')
        else:
            notice_history = MonitorNotice.objects.filter(monitor_id=monitor_id).order_by('-id')
        notice_list_history = []
        if notice_history:
            for item in notice_history:
                dict_add = {}
                dict_add.update({
                    'id': item.id,
                    'title': item.title,
                    # 'create_time': item.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                })
                if item.create_time:
                    dict_add.update({'create_time': item.create_time.strftime('%Y-%m-%d %H:%M:%S')})
                status_template = '<span class="label label-{}" style="font-size: 100%">{}</span>'
                if item.status == '0':
                    dict_add.update(
                        {'status': status_template.format('success', item.get_status_display())})
                elif item.status == '1':
                    dict_add.update(
                        {'status': status_template.format('danger', item.get_status_display())})
                notice_list_history.append(dict_add)

        records_total = notice_history.count()

        data = {
            "draw": draw,
            "recordsTotal": records_total,
            "recordsFiltered": records_total,
            "data": notice_list_history[data_from:data_to],
        }
        return JsonResponse(data)
    else:
        data = {}
        return JsonResponse(data)


# to check json params correct

def check_params(param_dict):
    need_list = ['title',
                 'message',
                 'owner',
                 'module',
                 'comment',
                 'status',
                 ]
    for item in need_list:
        if not param_dict.get(item):
            return '{} is empty'.format(item)
    return ''
