from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)


def cookie(request: HttpRequest):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view = the zap cookie is ' + str(oldval))
    if oldval:
        # No expired date = until browser closes
        resp.set_cookie('zap', int(oldval)+1)
    else:
        resp.set_cookie('zap', 42)
    resp.set_cookie('ludius', 42, max_age=1000)  # seconds until expore

    return resp

def sessfun(request: HttpRequest):
    num_visits = request.session.get('num_visits',0) +1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count= ' + str(num_visits))
    return resp