from django.urls import path
from . import views

# from . 의 .은 현재 폴더를 의미.
# views 모듈을 불러와야 하므로 import 
# views 모듈의 함수 index를 사용하는 것 

# 앱의 urlpatterns에서는 include() 함수를 사용하지 않는다.
urlpatterns = [
	path('', views.index)
]