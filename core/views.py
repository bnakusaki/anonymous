from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# 
# @csrf_exempt
def demoPage(request):
    # user: User = User.objects.get(pk=1)
    # username = request.POST.get('username')
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    return JsonResponse({'name': 'username', 'email': 'email'})
