from django.contrib import admin
from .models import SurveyTwo, OptionTwo

@admin.register(SurveyTwo)
class SurveyTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    search_fields = ('question',)

@admin.register(OptionTwo)
class OptionTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_text', 'survey')
    search_fields = ('option_text',)
