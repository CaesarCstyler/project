from rest_framework import serializers
from applications.sneakers.models import Sneakers, SneakersImage, Order
from django.db.models import Avg

class SneakersImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SneakersImage
        fields = '__all__'


class SneakersSerializer(serializers.ModelSerializer):
    images = SneakersImageSerializer(many=True, read_only=True)

    class Meta:
        model = Sneakers
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']

        return representation

    def create(self, validated_data):
        sneakers = Sneakers.objects.create(**validated_data)

        request = self.context.get('request')
        data = request.FILES
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(SneakersImage(sneakers=sneakers, image=i))
        Sneakers.objects.bulk_create(image_objects)

        return sneakers



class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ('sneakers', 'quantity', 'description')
    