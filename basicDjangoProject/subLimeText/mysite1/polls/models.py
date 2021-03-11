from django.db import models
from django.utils import timezone
import datetime
# 여기에 정의된 모델(데이터베이스 테이블)은 migrate 명령을 이용하여
# 실제 데이터베이스에 적용할 수 있다.

# 2개의 모델 객체 생성(테이블)
class Question(models.Model):
	question_txt = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_txt

	# 가장 최근 데이터가 있는지 없는지를 판단하기 위한 메서드
	def published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
		# 하루를 뺀 값인 24시간 안에 있는 데이터가 있느냐 없느냐 확인하기 위한 방법.
		# 최신 데이터인지를 판단하는.


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


# Django 모델 API (데이터를 추가/갱신/조회)
# ORM (Object Relational Mapper) 
# insert : 객체생성후에 save() 함수를 이용하여 새객체를 insert한다.
# select : Django model class에 대해서 objects라는 Manager 객체를 자동으로 추가해준다.
# (특정 데이터 필터, 정렬 등 많은 것을 할 수 있다.)
# objects는 django.db.models.Manager 이다. 이 매니저 객체를 이용해서 데이터를 필터링 할 수 있고,
# 정렬을 할 수도 있으며, 기타 여러 기능들을 사용할 수 있다.
# 데이터를 읽어올 때 바로 이 매니저 객체를 사용하였음(모델클래스명.objects)
# all() : 테이블 데이터를 모두 가져온다. // Question.objects.all() 
# get() : 하나의 row만을 가져올 때 사용하는 메소드이다.
# Primary Key를 가져올 때는 Question.objects.get(pk = 1)
# filter() : 특정조건을 이용하여 Row들을 가져오기 위한 메소드 
# exclude() : 특정 조건을 제외한 나머지 Row들을 가져오기 위한 메소드 filter() 반대개념
# count() : 데이터의 갯수(row 수)를 세기위한 메소드 
# order_by() : 데이터를 어떤 특정 키에 따라서 정렬하기 위한 메소드, 정렬키를 인수로 사용하는데 아래와 같은 원칙이 있다.
# 원칙 : -가 붙으면 내림차순이 된다.
# 예를 들어서 Quesction의 id 값을 기준으로 정렬하고 싶을 때 
# Question.objects.order_by('-id') // 내림차순 // 출력해보고 기록해 놓기.