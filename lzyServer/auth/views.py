# -*- coding:utf8 -*-
import json,time,random,os
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from models import AuthenticatingCode


def auth_code(request):
    code = request.GET.get('code', '0')
    print code
    # for x in range(100):
    #     code = str(random.randrange(1000000000000000, 9999999999999999, 16))
    #     date = '1500400000'
    #     AuthenticatingCode.objects.create(auth_code=code, date=date)

    # print os.path.dirname(__file__)
    # print os.path.dirname(os.path.dirname(__file__))

    return_dict = {'code':0}
    obj = AuthenticatingCode.objects.filter(auth_code=code).first()
    if not obj:
        return_dict['code'] = -1
        return HttpResponse(json.dumps(return_dict), content_type='application/json')

    if int(obj.date) < int(time.time()):
        return_dict['code'] = 1
        return HttpResponse(json.dumps(return_dict), content_type='application/json')

    return HttpResponse(json.dumps(return_dict), content_type='application/json')

def auth_code_html(request):
    return render_to_response('auth/check.html', locals())