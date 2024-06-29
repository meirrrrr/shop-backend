from django.urls import path, include
from rest_framework.routers import DefaultRouter

from basic import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]

