from django.shortcuts import render
from django.http import HttpResponse
# 웹 서버 응답을 위해서 필요하다. 

from .models import Question
# Create your views here.

def index(request):
	questions = Question.objects.all()
	# str = ''
	# for question in questions:
	# 	str += "{}, 시간 : {} <br/>".format(question.question_txt, question.pub_date)
	# 	str += "---------------------------------------------------------------<br/>"

	# return HttpResponse(str)
	context = {'questions': questions}
	return render(request, 'temp_test/index.html', context)