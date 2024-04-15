from django.urls import path
from .views import SurveyCreateViewTwo, SurveyRetrieveUpdateDestroyViewTwo, AnswerCreateViewTwo, SurveyRetrieveBySlugView

urlpatterns = [
    path('surveytwo/', SurveyCreateViewTwo.as_view(), name='survey-two-create'),
    path('surveytwo/<int:pk>/', SurveyRetrieveUpdateDestroyViewTwo.as_view(), name='survey-two-detail'),
    path('surveytwo/<slug:slug>/', SurveyRetrieveBySlugView.as_view(), name='survey-retrieve-by-slug'),
    path('surveytwo/create/answer/', AnswerCreateViewTwo.as_view(), name='answer-create'),

]
