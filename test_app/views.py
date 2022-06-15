from django.shortcuts import render
from django.http import HttpResponse # 문자열을 보여주는 함수

# Create your views here.
def index(request):
    # return HttpResponse("test_app first page")
    return render(request,'test_app/index.html')