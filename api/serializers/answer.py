from rest_framework.serializers import ModelSerializer

from api.models import Answer
from api.serializers.input_type import InputTypeSerializer


class AnswerSerializer(ModelSerializer):

    input_type = InputTypeSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'name', 'label', 'initial_value', 'validation', 'sequence', 'created', 'modified', 'question', 'user', 'input_type']
