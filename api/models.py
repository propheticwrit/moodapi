import uuid

from django.db import models

from authentication.models import User


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False, default='')
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = 'category'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Survey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False, default='')
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    category = models.ManyToManyField(Category, related_name='surveys', blank=True)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"
        db_table = 'survey'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=False, default='')
    label = models.CharField(max_length=255, null=False, default='')
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    survey = models.ManyToManyField(Survey, related_name='questions', blank=True)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        db_table = 'question'
        ordering = ['id']

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class InputType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    type = models.CharField(max_length=100, null=False, default='Text')

    class Meta:
        verbose_name = "InputType"
        verbose_name_plural = "InputTypes"
        db_table = 'input_types'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=True)
    label = models.CharField(max_length=255, null=True)
    initial_value = models.CharField(max_length=255, null=True)
    validation = models.CharField(max_length=255, null=True)
    sequence = models.IntegerField(default=-1)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    input_type = models.ForeignKey(InputType, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question, related_name='answers', blank=True)
    user = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        db_table = 'answer'
        ordering = ['sequence']

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
        db_table = 'observation'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    complete = models.BooleanField(default=False)
    observation = models.ForeignKey(Observation, related_name='reports', on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        db_table = 'report'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Response(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    report = models.ForeignKey(Report, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        db_table = 'response'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class ResponseField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=255, null=False, default='')
    created = models.DateTimeField(null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)
    response = models.ForeignKey(Response, related_name='fields', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ResponseField"
        verbose_name_plural = "ResponseFields"
        db_table = 'response_fields'

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)
