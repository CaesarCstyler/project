from rest_framework import serializers
from applications.brand.models import Brand

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'
