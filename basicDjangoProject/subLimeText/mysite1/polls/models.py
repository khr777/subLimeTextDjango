from django.db import models

# 여기에 정의된 모델(데이터베이스 테이블)은 migrate 명령을 이용하여
# 실제 데이터베이스에 적용할 수 있다.

# 2개의 모델 객체 생성(테이블)
class Question(models.Model):
	question_txt = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)


