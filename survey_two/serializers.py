from rest_framework import serializers
from .models import SurveyTwo, OptionTwo, AnswerTwo
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionTwo
        fields = ['id', 'option_text']

class SurveyTwoSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = SurveyTwo
        fields = ['id', 'question', 'options', 'slug']

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        slug = slugify(validated_data['question'])
        if SurveyTwo.objects.filter(slug=slug).exists():
            slug += '-' + get_random_string(length=5)
        validated_data['slug'] = slug
        survey = SurveyTwo.objects.create(**validated_data)
        for option_data in options_data:
            OptionTwo.objects.create(survey=survey, **option_data)
        return survey

class SurveySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = SurveyTwo
        fields = ['id', 'question', 'options', 'slug', 'owner']

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        slug = slugify(validated_data['question'])
        if SurveyTwo.objects.filter(slug=slug).exists():
            slug += '-' + get_random_string(length=5)
        validated_data['slug'] = slug
        survey = SurveyTwo.objects.create(**validated_data)
        for option_data in options_data:
            OptionTwo.objects.create(survey=survey, **option_data)
        return survey

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerTwo
        fields = ['id', 'survey', 'choice']

class SurveyRetrieveBySlugSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = SurveyTwo
        fields = ['question', 'options']

    def get_options(self, obj):
        options = obj.options.all()
        return OptionSerializer(options, many=True).data