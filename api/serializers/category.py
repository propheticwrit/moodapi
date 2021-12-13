from rest_framework.serializers import ModelSerializer

from api.models import Category
from api.serializers.survey import SurveySerializer


class CategorySerializer(ModelSerializer):

    surveys = SurveySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'created', 'modified', 'user', 'surveys']
