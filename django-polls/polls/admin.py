from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

#
# class QuestionInfoAdmin(admin.ModelAdmin):
#     list_display = ['pk','question_text','pub_date']
# # class QuestionAdmin(admin.ModelAdmin):
# #     fieldsets = [
# #         (None,               {'fields': ['question_text']}),
# #         ('Date information', {'fields': ['pub_date']}),
# #     ]
# class ChoiceInfoAdmin(admin.ModelAdmin):
#     list_display = ['pk','votes','choice_text','question']
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
#
# admin.site.register(Question,QuestionInfoAdmin)
# # admin.site.register(Question,QuestionAdmin)
# # admin.site.register(Choice,ChoiceInfoAdmin)
# # admin.site.register(Choice,ChoiceInline)
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['pk', 'question_text', 'pub_date','was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)