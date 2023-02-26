from django.http import Http404
from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from applications.category.models import Category
from applications.category.serializers import CategorySerializer
from applications.category.permissions import IsAdmin
from applications.category.models import Category
from applications.sneakers.models import Sneakers
from applications.sneakers.serializers import SneakersSerializer
from applications.category.serializers import CategorySerializer

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        sneakers = Sneakers.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = SneakersSerializer(sneakers, many=True)
        return Response(serializer.data)
    else:
        return Response({'sneakers': []})


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]

    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
