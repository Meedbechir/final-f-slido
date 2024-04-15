from rest_framework import serializers
from .models import QuestionOne, AnswerOne

class QuestionOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOne
        fields = ['question_text', 'slug', 'created_at']

class AnswerOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOne
        fields = ['question', 'answer_text', 'created_at']
        
class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOne
        fields = ['question_text', 'created_at']
