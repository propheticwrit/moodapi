from rest_framework.serializers import ModelSerializer

from api.models import Question
from api.serializers.answer import AnswerSerializer


class QuestionSerializer(ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'name', 'label', 'created', 'modified', 'survey', 'user', 'answers']
