from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views.category import CategoryViewSet
from api.views.question import QuestionViewSet
from api.views.survey import SurveyViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'category', CategoryViewSet, 'Category')
router.register(r'survey', SurveyViewSet, 'Survey')
router.register(r'question', QuestionViewSet, 'Question')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('authentication.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
]
