from django.db import models


class TGUser(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="Telegram User ID")
    user_name = models.CharField(max_length=100, null=True, verbose_name="Telegram Username")
    first_name = models.CharField(max_length=100, null=True, verbose_name="First name")

    class Meta:
        verbose_name_plural = "Telegram Users"
        verbose_name = "Telegram User"

    def __str__(self):
        return str(self.user_id)


class BaseQuestions(models.Model):
    question_text = models.TextField(null=True, blank=True, verbose_name="Question")
    text = models.TextField(null=True, blank=True, verbose_name="Text")

    class Meta:
        abstract = True

    def __str__(self):
        return self.question_text


class BaseAnswers(models.Model):
    user_id = models.IntegerField(verbose_name="Telegram User ID")
    answers = models.JSONField(verbose_name="Answers")
    date = models.DateTimeField(verbose_name="Date and time")

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.user_id)


class QuestionsBAI(models.Model):
    question_text = models.CharField(max_length=255, verbose_name="Question")
    text = models.TextField(null=True, blank=True, verbose_name="Text")

    class Meta:
        verbose_name_plural = "BAI Questions"
        verbose_name = "BAI Question"

    def __str__(self):
        return self.question_text


class AnswersBAI(models.Model):
    user_id = models.IntegerField(verbose_name="Telegram User ID")
    answers = models.JSONField(verbose_name="Answers")
    result = models.IntegerField(verbose_name="Result BAI")
    date = models.DateTimeField(verbose_name="Date and time")

    class Meta:
        verbose_name_plural = "BAI Answers"
        verbose_name = "BAI Answer"

    def __str__(self):
        return str(self.answers)


class QuestionsWorkList(BaseQuestions):

    class Meta:
        verbose_name_plural = "Work List Questions"
        verbose_name = "Work List Question"


class QuestionsABCModel(BaseQuestions):

    class Meta:
        verbose_name_plural = "ABC Model Questions"
        verbose_name = "ABC Model Question"


class QuestionsFallingArrow(BaseQuestions):

    class Meta:
        verbose_name_plural = "Falling Arrow Questions"
        verbose_name = "Falling Arrow Question"


class QuestionsEmotions(BaseQuestions):

    class Meta:
        verbose_name_plural = "Emotions Questions"
        verbose_name = "Emotions Question"


class QuestionsHistory(BaseQuestions):

    class Meta:
        verbose_name_plural = "History Questions"
        verbose_name = "History Question"


class AnswersWorkList(BaseAnswers):

    class Meta:
        verbose_name_plural = "Work List Answers"
        verbose_name = "Work List Answer"


class AnswersABCModel(BaseAnswers):

    class Meta:
        verbose_name_plural = "ABC Model Answers"
        verbose_name = "ABC Model Answer"


class AnswersFallingArrow(BaseAnswers):

    class Meta:
        verbose_name_plural = "Falling Arrow Answers"
        verbose_name = "Falling Arrow Answer"


class AnswersEmotions(BaseAnswers):

    class Meta:
        verbose_name_plural = "Emotions Answers"
        verbose_name = "Emotions Answer"


class AnswersHistory(BaseAnswers):

    class Meta:
        verbose_name_plural = "History Answers"
        verbose_name = "History Answer"