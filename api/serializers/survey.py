from rest_framework.serializers import ModelSerializer

from api.models import Survey


class SurveySerializer(ModelSerializer):

    class Meta:
        model = Survey
        fields = '__all__'
