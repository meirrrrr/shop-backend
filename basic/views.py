from rest_framework import viewsets, permissions
from basic import models
from basic import serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.filter(is_active=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.AllowAny,)

