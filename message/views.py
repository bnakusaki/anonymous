from django.shortcuts import render
from .models import Message
from django.http import HttpResponse, JsonResponse
import json
# import pymysql
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# @csrf_exempt
def index(request):
    data = {'success': False}
    if request.method == 'POST':
        message = json.loads(request.body)
        p = Message(messages=message['message'])
        p.save()
        data['success'] = True
        print(message)
        return JsonResponse(message['message'], safe=False)
    if request.method == 'DELETE':
        Message.objects.all().delete()
        return HttpResponse('Contents Deleted')
    if request.method == 'GET':
        pass
