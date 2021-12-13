from rest_framework.serializers import ModelSerializer

from api.models import InputType


class InputTypeSerializer(ModelSerializer):

    class Meta:
        model = InputType
        fields = ['id', 'type']
