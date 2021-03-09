"""helloprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 역할 담당을 누가 할 것인지 지정하는 것.
# include() 함수는 다른 URLconf들을 참조할 수 있도록 도와주는 함수 
# Django에서 include() 함수를 사용하면 장고 자체 시스템에서 include 사용하게 되면, 
# URL 그 시점까지 일치하는 부분을 잘라내고 남은 문자열 부분을 URLconf로 전달한다.
# 지금 시점이 아닌, 남아있는 시점의 URL을 가져오겠다는 의미.

# include() 함수를 언제 사용할까?
# admin.site.urls 를 제외한 다른 urlPattern을 include할 때마다 사용한다.
urlpatterns = [
	path('hello/', include('hello.urls')), # URLconf = urls 
    path('admin/', admin.site.urls)
]