from rest_framework import generics
from applications.sneakers.models import Sneakers, SneakersImage
from applications.feedback.models import Like, Rating
from applications.sneakers.serializers import SneakersSerializer, SneakersImageSerializer, CommentSerializer
from applications.feedback.serializers import RatingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from applications.sneakers.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SneakersModelViewSet(ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    permission_classes = [IsOwner]

    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id', 'owner']

    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'

        if not like_obj.is_like:
            status = 'unliked'

        return Response({'status': status})


    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)



    def  perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        

class CreateImageAPIView(generics.CreateAPIView):
    queryset = SneakersImage.objects.all()
    serializer_class = SneakersImageSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(ViewSet):
    def list(self, request):
        comments = Sneakers.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



class CommentModelViewSet(ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
