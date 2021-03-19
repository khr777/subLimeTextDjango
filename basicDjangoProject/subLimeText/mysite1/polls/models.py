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
# Question.objects.order_by('-id', aa) 만약 id가 중복일 경우에는, aa 오름차순으로 정렬한다. 


# distinct() : 중복된 값을 하나로만 표시하기 위한 메서드 (동일한 이름이 2개일 경우, 1개만 표시하는) 
# SQL의 SELECT DISTINCT와 같은 기능의 메소드 
# rows = User.objects.distinct('name') // 중복되는 이름이 있을 경우, 이름 1개만 
# first() : 여러개의 데이터 중에서 처음에 있는 row만을 리턴한다. 
# first() 함수 예시 __ rows = User.objects.order_by('name').first() 
# 위의 결과는 정렬된 레코드(row)중에서 가장 첫번째 row가 리턴값이 된다. // 직접 출력해보기. 
# last() : 여러개의 데이터 중에서 마지막 row만을 리턴한다.
# row = Question.objects.order_by('-id').last() // 직접 출력해보기.

## 위의 메소드들은 실제 데이터 결과를 직접 리턴하기보다는 쿼리 표현식(QuerySet) 형태로 리턴한다. 
# 여러개의 메소드들을 계속해서 연결식으로 형태로 사용할 수 있다.(체인처럼 연결해서 사용할 수 있다는 의미)
# 따라서, 여러 메소드들을 체인처럼 연결해서 사용할 수 있다.

## row = User.objects.filter(name = 'Lee').order_by('-id').first() -> 위의 의미.

## 예제 시작 
# from django.utils import timezone
# current_year = timezone.now().year
# current_year 출력 : 2021 
# Question.objects.filter(pub_date__year = currernt_year).order_by('-id').last()



# update : 수정할 row 객체를 얻은 후에 변경할 필드를 수정한다. 
# 수정한 후에는 save() 메소드를 호출한다.
# SQL UPDATE가 실행되어 테이블에 데이터가 갱신된다. 
# 예제
# q = Question.objects.get(pk = 1)
# q.question_txt 
# 출력 : '뭘 좋아하시나요?'
# q.question_txt = "무슨 영화를 좋아하시나요?"
# q.save()
# q.question_txt 
# 출력 : '무슨 영화를 좋아하시나요?'
# Question.objects.all()
# 출력 : <QuerySet [<Question: 무슨 영화를 좋아하시나요?>, <Question: 좋아하시는 음식은?>, <Question: 어떤 스포츠를 좋아하니?>]>
# Tip : q.save()를 해주지 않으면 all() 코드를 실행시키면 데이터베이스의 데이터가 변경되지 않은 채로 출력된다. 


# delete : ROW의 객체를 얻은 후에 delete() 메소드를 호출한다. 
# save()를 할 필요가 없다. delete 메소드에 의해서 바로 데이터베이스의 레코드(row)가 삭제된다. 

