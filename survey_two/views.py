from rest_framework import generics
# from rest_framework import permissions
from .models import SurveyTwo, AnswerTwo
from .serializers import SurveySerializer, SurveyTwoSerializer, AnswerSerializer, SurveyRetrieveBySlugSerializer
from rest_framework.response import Response
from rest_framework import status

class SurveyCreateViewTwo(generics.ListCreateAPIView):
    queryset = SurveyTwo.objects.all()
    serializer_class = SurveySerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save() 

class SurveyRetrieveUpdateDestroyViewTwo(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyTwo.objects.all()
    serializer_class = SurveyTwoSerializer

class AnswerCreateViewTwo(generics.ListCreateAPIView):
    queryset = AnswerTwo.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save()
        
class SurveyRetrieveBySlugView(generics.RetrieveAPIView):
    serializer_class = SurveyRetrieveBySlugSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return SurveyTwo.objects.get(slug=slug)
        except SurveyTwo.DoesNotExist:
            return Response({"detail": "Survey not found."}, status=status.HTTP_404_NOT_FOUND)