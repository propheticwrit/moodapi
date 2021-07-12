from rest_framework.viewsets import ModelViewSet

from api.models import Survey
from api.serializers.survey import SurveySerializer


class SurveyViewSet(ModelViewSet):

    serializer_class = SurveySerializer
    queryset = Survey.objects.all()
