from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.mixins import APIMixin
from api.models import Category
from api.serializers.category import CategorySerializer


class CategoryViewSet(APIMixin, ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('parent_id')
    filterset_fields = ['user', 'parent_id']

    @action(detail=False, url_path='base')
    def base_categories(self, request):

        null_parents = Category.objects.filter(parent_id=None)

        null_parent_ids = null_parents.values_list('id', flat=True)

        null_children = self.queryset.filter(parent_id__in=null_parent_ids)

        base_categories = []
        for null_parent in null_parents:
            null_parent_dict = {null_parent.name: self.serializer_class(null_parent).data, 'children': []}
            for null_child in null_children.filter(parent_id=null_parent.id):
                null_parent_dict['children'].append(self.serializer_class(null_child).data)
            base_categories.append(null_parent_dict)

        return Response(base_categories)
