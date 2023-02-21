from rest_framework import serializers
from applications.sneakers.models import Sneakers, SneakersImage
from applications.feedback.models import Comment
from applications.feedback.serializers import LikeSerializer
from django.db.models import Avg

class SneakersImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SneakersImage
        fields = '__all__'


class SneakersSerializer(serializers.ModelSerializer):
    images = SneakersImageSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Sneakers
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like_count'] = instance.likes.filter(is_like=True).count()
        representation['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']

        return representation

    def create(self, validated_data):
        post = Sneakers.objects.create(**validated_data)

        request = self.context.get('request')
        data = request.FILES
        image_objects = []
        for i in data.getlist('images'):
            image_objects.append(SneakersImage(post=post, image=i))
        Sneakers.objects.bulk_create(image_objects)

        return post


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    
    class Meta:
        model = Comment
        fields = '__all__'
