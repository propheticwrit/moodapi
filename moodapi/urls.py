from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views.category import CategoryViewSet
from api.views.survey import SurveyViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'category', CategoryViewSet, 'Category')
router.register(r'survey', SurveyViewSet, 'Survey')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
