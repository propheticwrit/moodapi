from rest_framework.serializers import ModelSerializer

from api.models import Answer


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'label', 'text', 'sequence', 'style', 'question']
