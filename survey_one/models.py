from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.contrib.auth.models import User


class QuestionOne(models.Model):
    question_text = models.TextField()
    slug = models.SlugField(unique=True, max_length=255, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_one', default=1)


    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.slug:
            random_string = get_random_string(length=10)
            self.slug = slugify(f"{self.question_text}-{random_string}")
        super().save(*args, **kwargs)

class AnswerOne(models.Model):
    question = models.ForeignKey(QuestionOne, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text
