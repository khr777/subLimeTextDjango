from django.db import models
from django.utils import timezone
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
		return self.timezone.now() - datetime.timedelta(days = 1)
		# 하루를 뺀 값인 24시간 안에 있는 데이터가 있느냐 없느냐 확인하기 위한 방법.
		# 최신 데이터인지를 판단하는.


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


