from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, GradeViewSet, DocumentViewSet
router = DefaultRouter()


router.register(r'grade', GradeViewSet, basename='grade')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'document', DocumentViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
