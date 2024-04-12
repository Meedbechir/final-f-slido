from django.urls import path
from .views import QuestionListCreateViewOne, AnswerListCreateViewOne, AnswerListForQuestionViewOne, QuestionDetailView

urlpatterns = [
    path('questions/', QuestionListCreateViewOne.as_view(), name='question-list-create-one'),
    path('answers/', AnswerListCreateViewOne.as_view(), name='answer-list-create-one'),
    path('questions/<int:question_id>/answers/', AnswerListForQuestionViewOne.as_view(), name='answer-list-for-question-one'),
    path('question/<slug:slug>/', QuestionDetailView.as_view(), name='question-detail'),

]
