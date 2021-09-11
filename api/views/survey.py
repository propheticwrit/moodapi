from rest_framework.viewsets import ModelViewSet

from api.mixins import APIMixin
from api.models import Survey
from api.serializers.survey import SurveySerializer


class SurveyViewSet(APIMixin, ModelViewSet):

    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
    filterset_fields = ['category', 'user']
