from django.contrib import admin
from .models import *


class TGUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'first_name')
    list_display_links = ('user_id', 'user_name', 'first_name')


class QuestionsWorkListAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class QuestionsABCModelAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class QuestionsBAIAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class QuestionsFallingArrowAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class QuestionsEmotionsAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class QuestionsHistoryAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'text')
    list_display_links = ('question_text', 'text')


class AnswersWorkListAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'date')
    list_display_links = ('user_id',)


class AnswersABCModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'date')
    list_display_links = ('user_id',)


class AnswersBAIAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'result', 'date')
    list_display_links = ('user_id',)


class AnswersFallingArrowAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'date')
    list_display_links = ('user_id',)


class AnswersEmotionsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'date')
    list_display_links = ('user_id',)


class AnswersHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'answers', 'date')
    list_display_links = ('user_id',)


admin.site.register(TGUser, TGUserAdmin)
admin.site.register(QuestionsWorkList, QuestionsWorkListAdmin)
admin.site.register(QuestionsABCModel, QuestionsABCModelAdmin)
admin.site.register(QuestionsBAI, QuestionsBAIAdmin)
admin.site.register(QuestionsFallingArrow, QuestionsFallingArrowAdmin)
admin.site.register(QuestionsEmotions, QuestionsEmotionsAdmin)
admin.site.register(QuestionsHistory, QuestionsHistoryAdmin)
admin.site.register(AnswersWorkList, AnswersWorkListAdmin)
admin.site.register(AnswersABCModel, AnswersABCModelAdmin)
admin.site.register(AnswersBAI, AnswersBAIAdmin)
admin.site.register(AnswersFallingArrow, AnswersFallingArrowAdmin)
admin.site.register(AnswersEmotions, AnswersEmotionsAdmin)
admin.site.register(AnswersHistory, AnswersHistoryAdmin)