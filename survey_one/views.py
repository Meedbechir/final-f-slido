from django.http import Http404
from rest_framework import generics, views, permissions
from rest_framework.response import Response
from .models import QuestionOne, AnswerOne
from .serializers import QuestionOneSerializer, AnswerOneSerializer, QuestionDetailSerializer

class QuestionListCreateViewOne(generics.ListCreateAPIView):
    queryset = QuestionOne.objects.all()
    serializer_class = QuestionOneSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 


class AnswerListCreateViewOne(generics.ListCreateAPIView):
    queryset = AnswerOne.objects.all()
    serializer_class = AnswerOneSerializer

class AnswerListForQuestionViewOne(generics.ListAPIView):
    serializer_class = AnswerOneSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return AnswerOne.objects.filter(question_id=question_id)

class QuestionDetailView(views.APIView):

    def get(self, request, slug, format=None):
        try:
            question = QuestionOne.objects.get(slug=slug)
        except QuestionOne.DoesNotExist:
            raise Http404("Question does not exist")

        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)
