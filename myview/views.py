from django.http import HttpResponse

def hello(resquest):
    return HttpResponse('Hello,world!')