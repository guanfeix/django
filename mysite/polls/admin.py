from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','question_text','pub_date']

class ChoiceInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','votes','choice_text','question']

admin.site.register(Question,QuestionInfoAdmin)
admin.site.register(Choice,ChoiceInfoAdmin)