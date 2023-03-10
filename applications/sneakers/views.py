from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from applications.sneakers.models import Sneakers, SneakersImage
from applications.feedback.models import Rating
from applications.sneakers.serializers import SneakersSerializer, SneakersImageSerializer
from applications.feedback.serializers import RatingSerializer
from applications.sneakers.permissions import IsAdmin

class LatestSneakersList(APIView):
    def get(self, request, format=None):
        sneakers = Sneakers.objects.all()[0:4]
        serializer = SneakersSerializer(sneakers, many=True)
        return Response(serializer.data)

class SneakersDetail(APIView):
    def get_object(self, category_slug, sneakers_slug):
        try:
            return Sneakers.objects.filter(category__slug=category_slug).get(slug=sneakers_slug)
        except Sneakers.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, sneakers_slug, format=None):
        sneakers = self.get_object(category_slug, sneakers_slug)
        serializer = SneakersSerializer(sneakers)
        return Response(serializer.data)

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SneakersModelViewSet(ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    permission_classes = [IsAdmin]

    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, sneakers_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)
        

class CreateImageAPIView(generics.CreateAPIView):
    queryset = SneakersImage.objects.all()
    serializer_class = SneakersImageSerializer
    permission_classes = [IsAdmin]
