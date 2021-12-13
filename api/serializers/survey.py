from rest_framework.serializers import ModelSerializer

from api.models import Survey
from api.serializers.question import QuestionSerializer


class SurveySerializer(ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'created', 'modified', 'category', 'user', 'questions']
