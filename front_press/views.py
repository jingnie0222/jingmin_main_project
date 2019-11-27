# Create your views here.
from django.http import HttpResponseRedirect
from user_record.views import login_checker
from django.shortcuts import render
from .models import FrontPressModel
from .forms import FrontPressForm
from user_record.models import user_record


# Create your views here.
@login_checker
def mission_list(request):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    if request.method == 'POST':
        mission_list = FrontPressModel.objects.all()

    elif request.method == 'GET':
        mission_list = FrontPressModel.objects.all()
        print("[Front_Press]ALL:", mission_list)
    return_dict = {
        # 'mission_filter': mission_filter,
        'mission_list': mission_list,
        'user_info': user_info,
    }
    return render(request, 'front_press/mission_list.html', return_dict)


@login_checker
def mission_add(request):
    user_info = {}
    uid = request.COOKIES.get("uid")
    if uid:
        user_info = user_record.objects.filter(uid=uid).values('name', 'uno', "uid")[0]
    if request.method == 'POST':
        front_press_form = FrontPressForm(request.POST)
        if front_press_form.is_valid():
            author = user_info['name']
            code = front_press_form.cleaned_data['code']
            type = front_press_form.cleaned_data['type']
            data_path = front_press_form.cleaned_data['data_path']

            new_mission = FrontPressModel.objects.create(
                author=author,
                code=code,
                type=type,
                data_path=data_path,
                status='0',
            )
            print("[Press_Front]Create Mission")
            return_url = 'http://fs.sogou/front_press/mission_list/'
            return HttpResponseRedirect(return_url)
        else:
            new_mission = FrontPressModel.objects.create(
                author=author,
                code=code,
                type=type,
                data_path=data_path,
                status='4',
            )
            print("[Press_Front]params not valid")
            return_url = 'http://fs.sogou/front_press/mission_list/'
            return HttpResponseRedirect(return_url)

    else:
        front_press_form = FrontPressForm()
    return_dict = {'front_press_form': front_press_form,
                   'user_info': user_info,
                   }
    return render(request, 'front_press/mission_add.html', return_dict)
