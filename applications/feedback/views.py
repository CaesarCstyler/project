from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from applications.feedback.models import Favorite, Comment
from applications.sneakers.models import Sneakers
from applications.feedback.serializers import FavoriteSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class FavoriteModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

class CommentViewSet(ViewSet):
    def list(self, request):
        comments = Sneakers.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
