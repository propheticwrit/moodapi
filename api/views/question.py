from rest_framework.viewsets import ModelViewSet

from api.models import Question
from api.serializers.question import QuestionSerializer


class QuestionViewSet(ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_fields = ['survey', 'user']
