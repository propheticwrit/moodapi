from rest_framework.viewsets import ModelViewSet

from api.mixins import APIMixin
from api.models import Category
from api.serializers.category import CategorySerializer


class CategoryViewSet(APIMixin, ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_fields = ['user']
