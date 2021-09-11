from rest_framework.viewsets import ModelViewSet

from api.mixins import APIMixin
from api.models import Question
from api.serializers.question import QuestionSerializer


class QuestionViewSet(APIMixin, ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_fields = ['survey', 'user']
