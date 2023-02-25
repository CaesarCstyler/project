from rest_framework import serializers
from applications.category.models import Category
from applications.sneakers.serializers import SneakersSerializer

class CategorySerializer(serializers.ModelSerializer):
    sneakers = SneakersSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "sneakers",
        )
