from django.db import models

# 2개의 모델 객체 생성(테이블)
class Question(models.Model):
	question_txt = models.CharField(max_Length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_Length=200)
	votes = models.IntegerField(default=0)


