from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from autoFront.models import Auto, front_diff_mission_result,Selftest
from user_record.views import login_checker
from user_record.models import user_record
import json, time
from autoFront import pagination


def auto(request):
    auto = Auto.objects.order_by('id')[::-1]

    page = request.GET.get('page')
    current_page = 1
    if page:
        current_page = int(page)

    page_obj = pagination.Page(current_page, len(auto), 8, 9)
    data = auto[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('?page=')

    return render(request, 'autoFront/auto.html', {'list': data,'page_str':page_str})


@csrf_exempt
@login_checker
def auto_add(request):
    if request.COOKIES.get("uid"):
        uid = request.COOKIES.get("uid")
    else:
        uid='fanghuizhi'
    # uid = request.COOKIES.get("uid")
    # uid = 'gongyanli'

    ret = {'status': True, 'error': None, 'data': None}

    isPic = 0
    isPagetest = 0
    isInterface = 0
    isPress = 0
    isUts = 0

    baseNode = request.POST.get('baseNode')
    baseNginx = request.POST.get('baseNginx')
    testNode = request.POST.get('testNode')
    testNginx = request.POST.get('testNginx')
    if request.POST.get('confIp'):
        confIp = request.POST.get('confIp')
    else:
        confIp=''
    if request.POST.get('confUser'):
        confUser = request.POST.get('confUser')
    else:
        confUser=''
    if request.POST.get('confPass'):
        confPass = request.POST.get('confPass')
    else:
        confPass=''
    if request.POST.get('confPath'):
        confPath = request.POST.get('confPath')
    else:
        confPath=''
    if request.POST.get('dataIp'):
        dataIp = request.POST.get('dataIp')
    else:
        dataIp=''
    if request.POST.get('dataUser'):
        dataUser = request.POST.get('dataUser')
    else:
        dataUser=''
    if request.POST.get('dataPass'):
        dataPass = request.POST.get('dataPass')
    else:
        dataPass=''
    if request.POST.get('dataPath'):
        dataPath = request.POST.get('dataPath')
    else:
        dataPath=''
    if request.POST.get('tag'):
        tag = request.POST.get('tag')
    else:
        tag=''

    radio = request.POST.get('typeRadios')

    checkbox = request.POST.getlist('typeCheck[]')
    print(checkbox)
    print(dataIp)
    for i in checkbox:
        if i == 'pic':
            isPic = 1
        elif i == 'pagetest':
            isPagetest = 1
        elif i == 'interface':
            isInterface = 1
        elif i == 'press':
            isPress = 1
        else:
            isUts = 1

    try:
        if uid:
            Auto.objects.create(baseNode=baseNode, baseNginx=baseNginx, testNode=testNode, testNginx=testNginx,
                                confIp=confIp, confUser=confUser, confPass=confPass, confPath=confPath, dataIp=dataIp,
                                dataUser=dataUser, dataPass=dataPass, dataPath=dataPath, type=radio, isPic=isPic,
                                isPagetest=isPagetest, isInterface=isInterface, isPress=isPress, isUts=isUts,
                                create_time=get_now_time(), tag=tag, user=uid)
    except Exception as e:
        print(e)
        ret['error'] = "Error:" + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


@login_checker
def auto_detail(request, task_id):
    task_detail = Auto.objects.filter(id=task_id)

    return render(request, 'autoFront/detail.html', {'auto_detail': task_detail})


def auto_detailInterface(request, task_id):
    task_detailInterface = front_diff_mission_result.objects.filter(mission_id=task_id).filter(is_diff=1)

    page = request.GET.get('page')
    current_page = 1
    if page:
        current_page = int(page)

    page_obj = pagination.Page(current_page, len(task_detailInterface), 4, 9)
    data = task_detailInterface[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('?page=')

    return render(request, 'autoFront/detailInterface.html',
                  {'auto_detail': data, 'page_str': page_str})


@csrf_exempt
@login_checker
def auto_del(request):
    ret = {'status': True, 'error': None, 'data': None}
    req_id = request.POST.get('line_id')
    try:
        Auto.objects.filter(id=req_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
        print(e)
    return HttpResponse(json.dumps(ret))


@csrf_exempt
@login_checker
def auto_cancel(request):
    ret = {'status': True, 'error': None, 'data': None}
    req_id = request.POST.get('line_id')
    try:
        Auto.objects.filter(id=req_id).update(status=6)
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
    return HttpResponse(json.dumps(ret))


def get_now_time():
    timeArray = time.localtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
def selftest(request):
    auto = Selftest.objects.order_by('id')[::-1]

    page = request.GET.get('page')
    current_page = 1
    if page:
        current_page = int(page)

    page_obj = pagination.Page(current_page, len(auto), 8, 9)
    data = auto[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('?page=')

    return render(request, 'autoFront/stauto.html', {'list': data,'page_str':page_str})


@csrf_exempt
@login_checker
def selftest_add(request):
    if request.COOKIES.get("uid"):
        uid = request.COOKIES.get("uid")
    else:
        uid='fanghuizhi'
    # uid = request.COOKIES.get("uid")
    # uid = 'gongyanli'

    ret = {'status': True, 'error': None, 'data': None}

    isPic = 0
    isPagetest = 0
    isInterface = 0
    isPress = 0
    isUts = 0

    isJuhe=0
    isStruct=0
    isRealmonitor=0
    isPingback=0
    isSecurity=0
    isDeadlink=0
    '''
    isJuhe=models.IntegerField(default=0)
    isStruct=models.IntegerField(default=0)
    isRealmonitor=models.IntegerField(default=0)
    isPingback=models.IntegerField(default=0)
    isSecurity=models.IntegerField(default=0)
    isDeaklink=models.IntegerField(default=0)
    '''
    baseNode = request.POST.get('baseNode')
    baseNginx = request.POST.get('baseNginx')
    testNode = request.POST.get('testNode')
    testNginx = request.POST.get('testNginx')
    if request.POST.get('baseIp'):
        baseIp = request.POST.get('baseIp')
    else:
        baseIp=''
    if request.POST.get('baseUser'):
        baseUser = request.POST.get('baseUser')
    else:
        baseUser=''
    if request.POST.get('basePass'):
        basePass = request.POST.get('basePass')
    else:
        basePass=''
    if request.POST.get('testIp'):
        testIp = request.POST.get('testIp')
    else:
        testIp=''
    if request.POST.get('testUser'):
        testUser = request.POST.get('testUser')
    else:
        testUser=''
    if request.POST.get('testPass'):
        testPass = request.POST.get('testPass')
    else:
        testPass=''
    if request.POST.get('tag'):
        tag = request.POST.get('tag')
    else:
        tag=''

    skip=request.POST.get('skipRadios')
    if skip=='execute':
        isSkipdeploy=0
    elif skip =='skip':
        isSkipdeploy=1

    radio = request.POST.get('typeRadios')

    checkbox = request.POST.getlist('typeCheck[]')
    print(checkbox)
    for i in checkbox:
        if i == 'pic':
            isPic = 1
        elif i == 'pagetest':
            isPagetest = 1
        elif i == 'interface':
            isInterface = 1
        elif i == 'press':
            isPress = 1
        elif i == 'uts':
            isUts = 1
        elif i == 'juhe':
            isJuhe = 1
        elif i == 'struct':
            isStruct = 1
        elif i == 'realmonitor':
            isRealmonitor = 1
        elif i == 'pingback':
            isPingback = 1
        elif i == 'security':
            isSecurity = 1
        elif i == 'deadlink':
            isDeadlink = 1

    try:
        if uid:
            Selftest.objects.create(baseNode=baseNode, baseNginx=baseNginx, testNode=testNode, testNginx=testNginx,
                                baseIp=baseIp, baseUser=baseUser, basePass=basePass, testIp=testIp,
                                testUser=testUser, testPass=testPass, isSkipdeploy=isSkipdeploy, type=radio, isPic=isPic,
                                isPagetest=isPagetest, isInterface=isInterface, isPress=isPress, isUts=isUts,
                                isJuhe=isJuhe, isStruct=isStruct, isRealmonitor=isRealmonitor, 
                                isPingback=isPingback,isSecurity=isSecurity,isDeadlink=isDeadlink,
                                create_time=get_now_time(), tag=tag, user=uid)
    except Exception as e:
        print(e)
        ret['error'] = "Error:" + str(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


def selftest_detail(request, task_id):
    task_detail = Selftest.objects.filter(id=task_id)
    return render(request, 'autoFront/stdetail.html', {'auto_detail': task_detail})


@csrf_exempt
@login_checker
def selftest_del(request):
    ret = {'status': True, 'error': None, 'data': None}
    req_id = request.POST.get('line_id')
    try:
        Selftest.objects.filter(id=req_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
        print(e)
    return HttpResponse(json.dumps(ret))


@csrf_exempt
@login_checker
def selftest_cancel(request):
    ret = {'status': True, 'error': None, 'data': None}
    req_id = request.POST.get('line_id')
    try:
        Selftest.objects.filter(id=req_id).update(status=6)
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
    return HttpResponse(json.dumps(ret))
