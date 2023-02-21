from rest_framework import serializers
from applications.sneakers.models import Sneakers, SneakersImage
from applications.feedback.models import Comment
from applications.feedback.serializers import LikeSerializer
from django.db.models import Avg

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SneakersImage
        fields = '__all__'
        # fields = ('id', )
        # exclude = ('post',)


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField()
    images = PostImageSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Sneakers
        # fields = ('title', )
        fields = '__all__'

    def to_representation(self, instance):
        # print(instance)
        representation = super().to_representation(instance)
        # print(representation)
        representation['like_count'] = instance.likes.filter(is_like=True).count()

        # rating_result = 0
        # for rating in instance.ratings.all(): # post1 (r1 - 2, r2 - 2, r3 - 2)
        #     rating_result += rating.rating

        # if rating_result:
        #     representation['rating'] = rating_result / instance.ratings.all().count()
        # else:
        #     representation['rating'] = rating_result

        representation['rating'] = instance.ratings.all().aggregate(Avg('rating'))['rating__avg']

        # print(representation['likes'])
        # for like in representation['likes']:
        #     if not like['is_like']:
        #         representation['likes'].remove(like)
        # representation['name'] = 'John'
        # representation['owner'] = instance.owner.email
        return representation

    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user # request.user
    #     # print(validated_data)
    #     return super().create(validated_data)

    def create(self, validated_data):
        post = Sneakers.objects.create(**validated_data)

        request = self.context.get('request')
        data = request.FILES
        # for i in data.getlist('images'):
        #     PostImage.objects.create(post=post, image=i)
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
