from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_record.views import login_checker
from .forms import mission_filter_forms, mission_add_forms
from .models import vr_query_mission
from user_record.models import user_record
import requests
import json


# Create your views here.
@login_checker
def mission_list(request):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    if request.method == 'POST':
        # 从forms中接收参数
        mission_filter = mission_filter_forms(request.POST)
        if mission_filter.is_valid():
            mission_query_from = mission_filter.cleaned_data['mission_query_from']
            mission_user = mission_filter.cleaned_data['mission_user']
            mission_status = mission_filter.cleaned_data['mission_status']
            mission_list = vr_query_mission.objects.all()
            if mission_query_from:
                mission_list = mission_list.filter(query_from=mission_query_from)
            if mission_user:
                mission_list = mission_list.filter(user=mission_user)
            if mission_status:
                mission_list = mission_list.filter(mission_status=mission_status)
            print(mission_user, mission_status)
        else:
            pass
    elif request.method == 'GET':
        mission_filter = mission_filter_forms()
        mission_list = vr_query_mission.objects.all()
        k = vr_query_mission.objects.filter(mission_id=74)
        for i in k:
            print(dir(i.mission_status))
            print(i.get_mission_status_display())
    return_dict = {'mission_filter': mission_filter,
                   'mission_list': mission_list,
                   'user_info': user_info,
                   }
    return render(request, 'vr_query/mission_list.html', return_dict)


@login_checker
def mission_add(request):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    if request.method == 'POST':
        mission_config_forms = mission_add_forms(request.POST)
        if mission_config_forms.is_valid():
            mission_type = mission_config_forms.cleaned_data['mission_type']
            vrid_mode = mission_config_forms.cleaned_data['vrid_mode']
            vrid_preserved = mission_config_forms.cleaned_data['vrid_preserved']
            vrid_url = mission_config_forms.cleaned_data['vrid_url']
            vrid_custom = mission_config_forms.cleaned_data['vrid_custom']
            query_from = mission_config_forms.cleaned_data['query_from']
            query_count = mission_config_forms.cleaned_data['query_count']
            query_count_for_7 = mission_config_forms.cleaned_data['query_count_for_7']
            query_count_for_multi = mission_config_forms.cleaned_data['query_count_for_multi']
            result_format = mission_config_forms.cleaned_data['result_format']
            result_order = mission_config_forms.cleaned_data['result_order']
            result_encode = mission_config_forms.cleaned_data['result_encode']

            form_errors = []
            vrid_list = []
            if vrid_mode == '0':
                vrid_preserved_url_list = {
                    '0': 'http://10.153.54.80:81/vrid_preserved/internal.txt',
                    '1': 'http://10.153.54.80:81/vrid_preserved/external.txt',
                    '2': 'http://10.153.54.80:81/vrid_preserved/jiegouhua.txt',
                    '3': 'http://10.153.54.80:81/vrid_preserved/zhilifang.txt',
                    '4': 'http://10.153.54.80:81/vrid_preserved/multihit00.txt',
                    '5': 'http://10.153.54.80:81/vrid_preserved/multihitXX.txt',
                }
                for pre in vrid_preserved:
                    pre_url = vrid_preserved_url_list.get(pre)
                    if pre_url:
                        pre_req = requests.get(url=pre_url)
                        vrid_list += pre_req.text.split('\n')
            elif vrid_mode == '1':
                vrid_req = requests.get(url=vrid_url)
                if vrid_req.status_code == 200:
                    vrid_list = vrid_req.text.split('\n')
            elif vrid_mode == '2':
                if vrid_custom and len(vrid_custom) >= 8:
                    vrid_list = vrid_custom.split('\r\n')
            if result_format:
                result_format_list = ['query', 'vrid'] + result_format.split(',')
            else:
                result_format_list = ['query', 'vrid']

            if not form_errors:
                new_mission = vr_query_mission.objects.create(
                    mission_type=mission_type,
                    query_from=query_from,
                    vrid_list=vrid_list,
                    query_count=str(query_count),
                    query_count_for_7=str(query_count_for_7),
                    order=result_order,
                    result_format=result_format,
                    result_encode=result_encode,
                    user=user_info['uid'],
                    mission_status='Waiting',
                )
                print(new_mission.mission_id)
                print(new_mission.start_time)




                if mission_type == 'query_for_id':
                    print("[VrQuery]QUERY_FOR_ID")
                    post_dict = {
                        'mission_id': new_mission.mission_id,
                        'query_from': query_from,
                        'vrid_list': vrid_list,
                        'query_count': str(query_count),
                        'query_count_for_7': str(query_count_for_7),
                        'order': result_order,
                        'result_format': result_format_list,
                        'result_encode': result_encode,
                        'user': user_info['uid']
                    }
                    post_json = json.dumps(post_dict)
                    post_req = requests.post('http://10.153.54.80:8888/get_query/', data=post_json)
                elif mission_type == 'multi_id_query':
                    print("[VrQuery]MULTI_ID_QUERY")
                    post_dict = {
                        'mission_id': new_mission.mission_id,
                        'query_from': query_from,
                        'vrid_list': vrid_list,
                        'query_count': str(query_count_for_multi),
                        'order': result_order,
                        'result_format': result_format_list,
                        'result_encode': result_encode,
                        'user': user_info['uid']
                    }
                    post_json = json.dumps(post_dict)
                    post_req = requests.post('http://10.153.54.80:8888/multi_id_query/', data=post_json)
                if post_req.status_code == 200:
                    print("[VrQuery]Mission INITIAL OK")
                    return_url = 'http://fs.sogou/vr_query/mission_list'
                else:
                    print("[VrQuery]Mission INITIAL FAILED")
                    new_mission.mission_status = 'Failed'
                return HttpResponseRedirect(return_url)
            #print(vrid_mode)
            #print(vrid_preserved)
            #print(vrid_url)
            #print(vrid_custom)
            #print(query_from)
            #print(query_count)
            #print(query_count_for_7)
            #print(result_format)
            #print(result_order)
            #print(result_encode)
        else:
            print('not PASSED')

    else:
        mission_config_forms = mission_add_forms()
    return_dict = {'mission_config_forms': mission_config_forms,
                   'user_info': user_info,
                   }
    return render(request, 'vr_query/mission_add.html', return_dict)
