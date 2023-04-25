from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns=[
    path('',views.myapp, name='myapp'), #views안의 myapp파일과 연결

]