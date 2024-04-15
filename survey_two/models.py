from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

class SurveyTwo(models.Model):
    question = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, blank=True, editable=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='surveys', default=1)


    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        slug = slugify(self.question)
        if SurveyTwo.objects.filter(slug=slug).exists():
            slug += '-' + get_random_string(length=5)
        self.slug = slug
        super().save(*args, **kwargs)

class OptionTwo(models.Model):
    survey = models.ForeignKey(SurveyTwo, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=200)

    def __str__(self):
        return self.option_text

class AnswerTwo(models.Model):
    survey = models.ForeignKey(SurveyTwo, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.survey.question} - {self.choice}"
