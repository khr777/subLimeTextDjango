from django.shortcuts import render
from django.http import HttpResponse

# index 함수를 활용
def index(request):
	return HttpResponse("hello django!!")
