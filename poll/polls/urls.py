from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [ 
	path('',views.index,name='index'),
        path('<int:faculty_id>/',views.detail,name='detail'),# /polls/5
        path('<int:faculty_id>/results' ,views.results,name='results'),
        path('<int:faculty_id>/vote',views.vote,name="vote"),
]
