from rest_framework.viewsets import ModelViewSet

from api.mixins import APIMixin
from api.models import Answer
from api.serializers.answer import AnswerSerializer


class AnswerViewSet(APIMixin, ModelViewSet):

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    filterset_fields = ['question', 'user']
