from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# index 함수를 활용
def index(request):
	# return HttpResponse("hello django!!")
	today = datetime.now().date()
	daysOfWeek = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
	context = {"today" : today, "daysOfWeek" : daysOfWeek}
	return render(request, 'hi.html', context)


