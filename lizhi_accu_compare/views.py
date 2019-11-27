from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.template import Template, Context
from user_record.models import user_record
from user_record.views import login_checker
from .models import LizhiAccuResult
from .models import LizhiAccuMission
from .forms import CaseDetailStatus, ListFilter
from .urlhandle import urlencode
from urllib import parse
import datetime
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
        mission_list = LizhiAccuMission.objects.all()

        # 从forms中接收参数
        # mission_filter = mission_filter_forms(request.POST)
        # if mission_filter.is_valid():
        #     mission_query_from = mission_filter.cleaned_data['mission_query_from']
        #     mission_user = mission_filter.cleaned_data['mission_user']
        #     mission_status = mission_filter.cleaned_data['mission_status']
        #     mission_list = vr_query_period.objects.all()
        #     if mission_query_from:
        #         mission_list = mission_list.filter(query_from=mission_query_from)
        #     if mission_user:
        #         mission_list = mission_list.filter(user=mission_user)
        #     if mission_status:
        #         mission_list = mission_list.filter(mission_status=mission_status)
        #     print(mission_user, mission_status)
        # else:
        #     pass
        pass
    elif request.method == 'GET':
        # mission_filter = mission_filter_forms()
        mission_list = LizhiAccuMission.objects.all()
        # k = LizhiAccuMission.objects.filter(mission_id=74)
        # for i in k:
        #     print(dir(i.mission_status))
        #     print(i.get_mission_status_display())
    return_dict = {
        # 'mission_filter': mission_filter,
        'mission_list': mission_list,
        'user_info': user_info,
    }
    return render(request, 'lizhi_accu_compare/mission_list.html', return_dict)


@login_checker
def mission_list_case(request, task_id):
    if request.method == 'GET':
        # print(task_id)
        case_list = LizhiAccuResult.objects.filter(task_id=task_id)
        return_dict = {
            'case_list': case_list,
        }
    else:
        return_dict = {
            'case_list': ''
        }
    return [request, 'lizhi_accu_compare/mission_list_case.html', return_dict]


def record_question(case_detail):
    """
    :param object:LizhiAccuResult object
    :return:
    """
    print("[Lizhi_Accu_Compare]Begin to INSERT")
    template = Template('''
<table class="table-bordered">
    <thead>
        <tr>
            <th style="width:10%;font-size: 16px">项目</th>
            <th style="width:44%;font-size: 16px">搜狗结果</th>
            <th style="width:2%"></th>
            <th style="width:44%;font-size: 16px">百度结果</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>现场样式</td>
            <td>
                <img class="img-responsive" src="{{ case_detail.sogou_pic }}" alt="Photo">
            </td>
            <td></td>
            <td>
                <img class="img-responsive" src="{{ case_detail.baidu_pic }}" alt="Photo">
            </td>
        </tr>
        <tr>
            <td>文字结果</td>
            <td>{{ case_detail.sogou_res }}</td>
            <td></td>
            <td>{{ case_detail.baidu_res }}</td>
        </tr>
    </tbody>
</table>
    ''')

    content = template.render(Context({'case_detail': case_detail}))
    itest_url = 'http://10.134.102.31/datacenter?op=add_onlinefault'
    # itest_url = 'http://10.134.104.40:5555'
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    url_content = {
        'title': case_detail.itest_record_title,
        'project_id': '345',
        'effect_type': '效果类',
        'duty': '数据问题',
        'level': 'bad case',
        'is_test': '线上存在',
        'type': '线上问题走查',
        'bug_start_time': now_time,
        'appearance': content, # 内容
        'email': 'yinjingjing@sogou-inc.com',
        'source': '测试自动化监控发现',
        'reason': '无',
        'todo': '无',
        'start_date': now_time,
    }

    post_data = parse.urlencode(url_content).replace('+', '%20')
    print(post_data)

    r = requests.post(url=itest_url, data=post_data)
    print("[Lizhi_Accu_Compare]", r.status_code, r.text)
    if r.status_code == 200:
        print("[Lizhi_Accu_Compare]", r.text)
        itest_record_id = json.loads(r.text).get('id', 0)
        if itest_record_id != 0:
            case_detail.itest_record_id = itest_record_id
            case_detail.save()
            return True
        else:
            return False
    else:
        return False


@login_checker
def mission_case_detail(request, task_id, query_id):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    print("[Lizhi_Accu_Compare]")
    if request.method == 'GET':
        print("[Lizhi_Accu_Compare]Read Details")
        case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
        first_case = LizhiAccuResult.objects.filter(task_id=task_id).first()
        last_case = LizhiAccuResult.objects.filter(task_id=task_id).last()
        first_id = first_case.query_id
        last_id = last_case.query_id
        print(first_id, last_id)
        prev_disable = ''
        next_disable = ''
        if query_id == first_id:
            prev_disable = 'disabled'
        if query_id == last_id:
            next_disable = 'disabled'
        if case_detail:
            case_detail = case_detail[0]
            case_detail_status = CaseDetailStatus(
                initial={
                    'status': case_detail.status,
                    'precision': case_detail.precision,
                    'comments': case_detail.comments,
                    'solve_time': case_detail.solve_time,
                    'lizhi_type': case_detail.lizhi_type,
                    'focus_member': case_detail.focus_member,
                    'itest_record_title': case_detail.itest_record_title,
                },
                instance=LizhiAccuResult
            )
        return_dict = {
            'case_detail_status': case_detail_status,
            'case_detail': case_detail,
            'prev_disable': prev_disable,
            'next_disable': next_disable,
        }
    elif request.method == 'POST':
        case_detail_status = CaseDetailStatus(request.POST)
        if case_detail_status.is_valid():
            status = case_detail_status.cleaned_data['status']
            precision = case_detail_status.cleaned_data['precision']
            solve_time = case_detail_status.cleaned_data['solve_time']
            comments = case_detail_status.cleaned_data['comments']
            lizhi_type = case_detail_status.cleaned_data['lizhi_type']
            focus_member = case_detail_status.cleaned_data['focus_member']
            itest_record_title = case_detail_status.cleaned_data['itest_record_title']
            # is_next = case_detail_status.cleaned_data['is_next']
            case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
            first_case = LizhiAccuResult.objects.filter(task_id=task_id).first()
            last_case = LizhiAccuResult.objects.filter(task_id=task_id).last()
            first_id = first_case.query_id
            last_id = last_case.query_id
            print(first_id, last_id)
            prev_disable = ''
            next_disable = ''
            if query_id == first_id:
                prev_disable = 'disabled'
            if query_id == last_id:
                next_disable = 'disabled'
            print("============", type(case_detail))
            if case_detail:
                case_detail = case_detail[0]
            # print(type(case_detail))
            case_detail.status = status
            case_detail.precision = precision
            case_detail.edit_member = user_info['name']
            case_detail.solve_time = solve_time
            case_detail.comments = comments
            case_detail.lizhi_type = lizhi_type
            case_detail.focus_member = focus_member
            case_detail.itest_record_title = itest_record_title
            case_detail.save()
            print(case_detail.status)
            if query_id == last_id:
                save_success = 'success_last'
            else:
                save_success = 'success'
            return_dict = {
                'case_detail_status': case_detail_status,
                'case_detail': case_detail,
                'prev_disable': prev_disable,
                'next_disable': next_disable,
                'save_success': save_success,
            }
            is_record = case_detail.itest_record_id
            if not is_record and user_info['uid'] in ['yinjingjing', 'liujinming'] and itest_record_title:
                print("[lizhi_Accu_Compare]INSERT")
                record_question(case_detail)
            else:
                print("[lizhi_Accu_Compare]Have Been Recorded")

        else:
            print("NOT VALID")
            case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
            first_case = LizhiAccuResult.objects.filter(task_id=task_id).first()
            last_case = LizhiAccuResult.objects.filter(task_id=task_id).last()
            first_id = first_case.query_id
            last_id = last_case.query_id
            print(first_id, last_id)
            prev_disable = ''
            next_disable = ''
            if query_id == first_id:
                prev_disable = 'disabled'
            if query_id == last_id:
                next_disable = 'disabled'
            print("============", type(case_detail))
            if case_detail:
                case_detail = case_detail[0]
            for i in case_detail_status:
                print(i)
                print(i.errors)
            return_dict = {
                'case_detail_status': case_detail_status,
                'case_detail': case_detail,
                'prev_disable': prev_disable,
                'next_disable': next_disable,
                'save_success': '',
            }
    else:
        return_dict = {
            'case_detail': ''
        }
    return [request, 'lizhi_accu_compare/mission_case_detail.html', return_dict]


@login_checker
def unsolved_case(request):
    if request.method == 'GET':
        case_list = LizhiAccuResult.objects.filter(status='0')
        print(case_list)
        list_filter = ListFilter()
        for i in case_list:
            print(i.task_id.task_id, i.query_id)
        return_dict = {
            'case_list': case_list,
            'list_filter': list_filter,
        }
    elif request.method == 'POST':
        case_list = LizhiAccuResult.objects.filter(status='0')
        print(case_list)
        list_filter = ListFilter(request.POST)
        if list_filter.is_valid():
            lizhi_type = list_filter.cleaned_data['lizhi_type']
            focus_member = list_filter.cleaned_data['focus_member']
            if lizhi_type and lizhi_type != '99':
                case_list = case_list.filter(lizhi_type=lizhi_type)
            if focus_member:
                case_list = case_list.filter(focus_member=focus_member)
        return_dict = {
            'case_list': case_list,
            'list_filter': list_filter,
        }
    else:
        return_dict = {
            'case_list': '',
            'list_filter': '',
        }
    return [request, 'lizhi_accu_compare/unsolved_case.html', return_dict]


def unsolved_next(request, query_id):
    if request.method == 'GET':
        status = request.GET.get("status")
        next_case = LizhiAccuResult.objects.filter(status=status, query_id__lt=query_id)[1:2]
        if next_case:
            next_id = next_case.query_id
    if next_id:
        return HttpResponseRedirect(reverse('lizhi_accu_compare:unsolved_detail' ))


def unsolved_prev(request, query_id):
    pass


def unsolved_detail(request, query_id):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    print("[Lizhi_Accu_Compare]")
    if request.method == 'GET':
        print("[Lizhi_Accu_Compare]Read Details")
        case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
        first_case = LizhiAccuResult.objects.filter(status='0').first()
        last_case = LizhiAccuResult.objects.filter(status='0').last()
        first_id = first_case.query_id
        last_id = last_case.query_id
        print(first_id, last_id)
        prev_disable = ''
        next_disable = ''
        if query_id == first_id:
            prev_disable = 'disabled'
        if query_id == last_id:
            next_disable = 'disabled'
        if case_detail:
            case_detail = case_detail[0]
            case_detail_status = CaseDetailStatus(
                initial={
                    'status': case_detail.status,
                    'precision': case_detail.precision,
                    'comments': case_detail.comments,
                    'solve_time': case_detail.solve_time,
                },
                instance=LizhiAccuResult
            )
        return_dict = {
            'case_detail_status': case_detail_status,
            'case_detail': case_detail,
            'prev_disable': prev_disable,
            'next_disable': next_disable,
        }
    elif request.method == 'POST':
        case_detail_status = CaseDetailStatus(request.POST)
        if case_detail_status.is_valid():
            status = case_detail_status.cleaned_data['status']
            precision = case_detail_status.cleaned_data['precision']
            solve_time = case_detail_status.cleaned_data['solve_time']
            comments = case_detail_status.cleaned_data['comments']
            lizhi_type = case_detail_status.cleaned_data['lizhi_type']
            focus_member = case_detail_status.cleaned_data['focus_member']
            print(lizhi_type)
            # is_next = case_detail_status.cleaned_data['is_next']
            case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
            first_case = LizhiAccuResult.objects.filter(status='0').first()
            last_case = LizhiAccuResult.objects.filter(status='0').last()
            first_id = first_case.query_id
            last_id = last_case.query_id
            print(first_id, last_id)
            prev_disable = ''
            next_disable = ''
            if query_id == first_id:
                prev_disable = 'disabled'
            if query_id == last_id:
                next_disable = 'disabled'
            print("============", type(case_detail))
            if case_detail:
                case_detail = case_detail[0]
            # print(type(case_detail))
            case_detail.status = status
            case_detail.precision = precision
            case_detail.edit_member = user_info['name']
            case_detail.solve_time = solve_time
            case_detail.comments = comments
            case_detail.lizhi_type = lizhi_type
            case_detail.focus_member = focus_member
            case_detail.save()
            print(case_detail.status)
            if query_id == last_id:
                save_success = 'success_last'
            else:
                save_success = 'success'
            return_dict = {
                'case_detail_status': case_detail_status,
                'case_detail': case_detail,
                'prev_disable': prev_disable,
                'next_disable': next_disable,
                'save_success': save_success,
            }
        else:
            print("NOT VALID")
            case_detail = LizhiAccuResult.objects.filter(query_id=query_id)
            first_case = LizhiAccuResult.objects.filter(status='0').first()
            last_case = LizhiAccuResult.objects.filter(status='0').last()
            first_id = first_case.query_id
            last_id = last_case.query_id
            print(first_id, last_id)
            prev_disable = ''
            next_disable = ''
            if query_id == first_id:
                prev_disable = 'disabled'
            if query_id == last_id:
                next_disable = 'disabled'
            print("============", type(case_detail))
            if case_detail:
                case_detail = case_detail[0]
            for i in case_detail_status:
                print(i)
                print(i.errors)
            return_dict = {
                'case_detail_status': case_detail_status,
                'case_detail': case_detail,
                'prev_disable': prev_disable,
                'next_disable': next_disable,
                'save_success': '',
            }
    else:
        return_dict = {
            'case_detail': ''
        }
    return [request, 'lizhi_accu_compare/mission_case_detail.html', return_dict]
