from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from datetime import datetime
from .models import user_record
import base64
import M2Crypto
import json
import os
import hashlib


# Create your views here.
def login(request, url='http://fs.sogou/R'):
    return HttpResponseRedirect("https://login.sogou-inc.com/?appid=1606&sso_redirect=" + url + "&targetUrl=")


def logout(request, url='http://fs.sogou/R_test'):
    response = HttpResponseRedirect(
        "https://login.sogou-inc.com/logout.jsp?appid=1606&sso_redirect=" + url + "&targetUrl=")
    response.delete_cookie('uid')
    response.delete_cookie('fuid')
    response.delete_cookie('pkid')
    return response


def login_checker(func, check="yes"):
    def checkuser(request, *args, **kwargs):
        fuid = request.COOKIES.get('fuid')
        pkid = request.COOKIES.get('pkid')
        params = request.GET.get('ptoken')
        # 有cookie 有params 跳转到 有cookie 无params
        # 无cookie 有params 跳转到 有cookie 无params
        # 无cookie 无params 跳转到 登录页面
        # 有cookie 有params 进行校验，校验通过允许访问(大多数逻辑))

        if fuid and pkid and not params:
            check_ok = False
            user_info = ptoken_analyser(pkid)
            if user_info:
                user_name = user_info.get("name")
                user_uid = user_info.get("uid")
                user_uno = user_info.get("uno")
                user_record.objects.get(name=user_name,
                                        uid=user_uid,
                                        uno=user_uno,
                                        )
                if user_record:
                    md5_str = user_uid + user_uno
                    uid_md5 = hashlib.md5(md5_str.encode()).hexdigest()
                    if uid_md5 == fuid:
                        check_ok = True
            if check_ok:
                print("[USER CHECK]CHECK OK, GO TO " + request.path)
                func_response = func(request, *args, **kwargs)
                # 进行后续操作，包括透传HttpResponse，渲染回传的list形式的render对象
                if isinstance(func_response, HttpResponse):
                    print("[USER CHECK][TYPE]HttpResponse")
                elif isinstance(func_response, list):
                    print("[USER CHECK][TYPE]list")
                    func_response[2].update(
                        {"user_info": user_record.objects.filter(uid=user_uid).values('name', 'uno', "uid")[0]})
                    func_response = render(func_response[0], func_response[1], func_response[2])
                return func_response
            else:
                print("[USER CHECK][COOKIES]VISIT " + request.path + " FAILED,NEED LOGIN")
                return logout(request, url="http://fs.sogou" + request.path)
        elif fuid and pkid and params:
            url = "http://fs.sogou" + request.path
            print("[USER CHECK][DROP PARAMS]REDIRECT")
            return HttpResponseRedirect(url)
        elif (not fuid or not pkid) and params:
            print("[USER CHECK][ONLY PARAMS]")
            cookies_ok = False
            ptoken = request.GET.get('ptoken')
            if ptoken:
                user_info = ptoken_analyser(ptoken)
                if user_info:
                    now = float(datetime.now().timestamp()) * 1000
                    ptoken_time = int(user_info['ts'])
                    if int(abs(now - ptoken_time)) < 3000:
                        cookies_ok = True
            if cookies_ok:
                user_name = user_info.get("name")
                user_uid = user_info.get("uid")
                user_uno = user_info.get("uno")
                print(user_name, user_uid, user_uno)
                user_record.objects.get_or_create(name=user_name,
                                                  uid=user_uid,
                                                  uno=user_uno,
                                                  )
                md5_str = user_uid + str(user_uno)
                fuid = hashlib.md5(md5_str.encode()).hexdigest()
                url = "http://fs.sogou" + request.path
                response = HttpResponseRedirect(url)
                response.set_cookie('uid', user_uid)
                response.set_cookie('fuid', fuid)
                response.set_cookie('pkid', ptoken)
                return response
            else:
                print("[USER CHECK][PARAM]VISIT " + request.path + " FAILED,NEED LOGIN")
                return logout(request, url="http://fs.sogou" + request.path)
        else:
            print("[USER CHECK][NO PARAMS AND COOKIES]VISIT " + request.path + " FAILED,NEED LOGIN")
            return logout(request, url="http://fs.sogou" + request.path)

    return checkuser


def ptoken_analyser(ptoken):
    """
    type: ptoken:str
    rtype: dict
    """
    # data = unquote(ptoken)
    data = ptoken
    # print(data)
    strcode = base64.b64decode(data)
    if os.path.exists('user_record/pub.pem'):
        pkey = M2Crypto.RSA.load_pub_key('user_record/pub.pem')
        output = pkey.public_decrypt(strcode, M2Crypto.RSA.pkcs1_padding).decode('utf8', 'ignore')
        output = json.loads(output)
    else:
        output = {}
    return output
