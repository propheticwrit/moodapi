from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Observation(models.Model):
    created = models.DateTimeField(null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Observation"
        verbose_name_plural = "Observations"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, default='')
    text = models.CharField(max_length=255, null=False, default='')

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class QuestionAnswerChoice(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=150, null=False, default='')
    response_code = models.CharField(max_length=100, null=False, default='')
    sequence = models.IntegerField(default=-1)

    class Meta:
        verbose_name = "QuestionAnswerChoice"
        verbose_name_plural = "QuestionAnswerChoices"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, default='')
    regex = models.CharField(max_length=100, null=False, default='')
    next_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True, related_name='next_question')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    complete = models.BooleanField(default=False)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=100, null=False, default='')

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
