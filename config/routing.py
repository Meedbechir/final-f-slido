from django.urls import path
from survey_one import consumers

websocket_urlpatterns = [
    path('ws/survey/', consumers.SurveyConsumer.as_asgi()),
]
    