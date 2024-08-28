from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz-list', views.quizList, name='quizList'),
    path('quiz-detail/<int:id>/', views.quizDetail, name='quizDetail'),
    path('create-quiz', views.createQuiz, name='createQuiz'),
    path('quizdelete/<int:id>/', views.quizDelete, name='deleteQuiz'),
    path('create-question/<int:id>/', views.questionCreate, name='questionCreate'),
    path('options-list/', views.optionList, name='optionsList'),
    path('optionDelete/<int:id>/', views.optionDelete, name='optionDelete'),
]