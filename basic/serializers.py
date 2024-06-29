from rest_framework import serializers

from basic import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Product
        exclude = ('is_active', 'created_at', 'updated_at', 'amount')
