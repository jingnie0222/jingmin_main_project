from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from hx_inner_wiki import models
from django.db.models import Q
#from utils import pagination
from hx_inner_wiki import pagination
import json, time, os, requests
from django.views.decorators.csrf import csrf_exempt
from .forms import EditorTestForm
from django.http import JsonResponse
from user_record.views import login_checker
from user_record.models import user_record
#import logging


# Create your views here.
@login_checker
def inner_wiki_list(request):
    #user_info = {}
    #uid = request.COOKIES.get("uid")
    #if uid:
    #    user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]

    #print("uid: ", uid)

    print("request.mothod_list is : ", request.method)
    if request.method == "GET":
        page = request.GET.get('page')
        tag = request.GET.get('tag')
        category = request.GET.get('category')
        current_page = 1
        if page:
            current_page = int(page)
        if tag and category == None:
            wiki_list = models.Hx_Inner_Wiki.objects.filter(Q(tag__icontains=tag)).order_by('-update_time')  # 模糊查询
        elif tag == None and category:
            wiki_list = models.Hx_Inner_Wiki.objects.filter(category=category).order_by('-update_time')
        else:
            wiki_list = models.Hx_Inner_Wiki.objects.all().order_by('-update_time')

        category_list = models.Hx_Inner_Wiki.objects.values('category').distinct()
        taglist = models.Hx_Inner_Wiki.objects.values('tag').distinct()
        tag_list = list()
        for item in taglist:
            if ',' in item['tag']:
                item['tag']=item['tag'].replace('，',',')
                tag_list += item['tag'].split(',')
            else:
                tag_list.append(item['tag'])
        tag_list = list(set(tag_list))
        page_obj = pagination.Page(current_page, len(wiki_list), 18, 9)
        data = wiki_list[page_obj.start:page_obj.end]
        #page_str = page_obj.page_str('/wiki/wiki?page=')
        page_str = page_obj.page_str('/hx_inner_wiki/inner_wiki_list?page=')
        #/testcache/task_queue
        #/hx_inner_wiki/inner_wiki_list/

        return_dict = {'form': data,
                      'page_str': page_str,
                      'category_list': category_list,
                      'tag_list': tag_list,
                      }

        #return render(request, 'hx_inner_wiki/inner_wiki_list.html', return_dict)
        return [request, 'hx_inner_wiki/inner_wiki_list.html', return_dict]


@login_checker
def inner_wiki_new(request):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]

    if (uid != ""):
        form = EditorTestForm()


    if request.method == "GET":
        return [request, 'hx_inner_wiki/inner_wiki_add.html', {'form': form}]
        #print("form: ", form)
     #   return render(request, 'hx_inner_wiki/inner_wiki_add.html', {'uid': uid, 'form': form})
    #return [request, 'hx_inner_wiki/inner_wiki_add.html', {'form': form}]



    if request.method == "POST":
        print("asdd")
        obj = models.Hx_Inner_Wiki.objects.create(user=uid, create_time=get_now_time(), update_time=get_now_time())
        form = EditorTestForm(request.POST, instance=obj)

        if form.is_valid():
            print("form is valid")
            # form.save()
            xx = form.save(commit=False)
            # xx.save()
            xx.user = uid
            xx.create_time = get_now_time()
            xx.save()
            form.save_m2m()
            print("sucess right now")
            return HttpResponseRedirect('/hx_inner_wiki/inner_wiki_list/')
            # return render(request, 'wiki/wiki_list.html', {'form': form})
            # return JsonResponse(dict(success=1, message="submit success!"))
        else:
            return JsonResponse(dict(success=0, message="submit error"))
    #else:
    #    form = EditorTestForm()
    #    return render(request, 'wiki/wiki_add.html', {'form': form})


@csrf_exempt
@login_checker
def inner_wiki_edit(request):
    user_id = request.COOKIES.get('uid')
    edit_id = request.GET.get('id')
    edit_content = models.Hx_Inner_Wiki.objects.get(id=edit_id)

    print("request.method_edit is: ", request.method)

    if request.method == "GET":
        form = EditorTestForm(instance=edit_content)
        return render(request, 'hx_inner_wiki/inner_wiki_add.html', {'form': form})
    if request.method == "POST":
        form = EditorTestForm(request.POST, instance=edit_content)
        if form.is_valid():
            wiki = form.save(commit=False)
            # form.title = request.POST.get('title')
            wiki.update_time = get_now_time()
            wiki.update_user = user_id
            wiki.save()
            return HttpResponseRedirect('/hx_inner_wiki/inner_wiki_list/')

            # return JsonResponse(dict(success=1, message="submit success!"))
        else:
            return JsonResponse(dict(success=0, message="submit error"))


@login_checker
def inner_wiki_detail(request, task_id):
    #print("tttt")
    try:
        info = models.Hx_Inner_Wiki.objects.filter(id=task_id)

        b = models.Hx_Inner_Wiki.objects.get(id=task_id)
        form = EditorTestForm(instance=b)

        wikitags = models.Hx_Inner_Wiki.objects.filter(id=task_id).values('tag')
        taglist = list()
        for item in wikitags:
            if ',' in item['tag']:
                tagsp = item['tag'].split(',')
                taglist += tagsp
            else:
                taglist.append(item['tag'])
        taglist = list(set(taglist))

        return_dict = {'form': form,
                      'taglist': taglist,
                      'info': info,
                      'task_id': task_id,
                      }
        return [request, 'hx_inner_wiki/inner_wiki_detail.html', return_dict]
        #return render(request, 'wiki/wiki_detail.html',
        #              {'form': form, 'taglist': taglist, 'info': info})
    except Exception as e:
        print(e)
        pass


        
@csrf_exempt
@login_checker
def inner_wiki_delete(request):
    
    ret = {'status': True, 'error': None, 'data': None}
    req_id = request.POST.get('line_id')
    #print("req_id: ", req_id)
    try:
        # models.Wiki.objects.filter(id=req_id).update(status=2)
        models.Hx_Inner_Wiki.objects.filter(id=req_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = "Error:" + str(e)
    return HttpResponse(json.dumps(ret))


def get_now_time():
    timeArray = time.localtime()
    #print("time is: ", time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
