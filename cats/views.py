from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .models import Cats, Breeds, Ratings
from .serializers import CatsSerializer, BreedsSerializer, RatingsSerializer


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BreedListCreateView(generics.ListCreateAPIView):
    queryset = Breeds.objects.all()
    serializer_class = BreedsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyPagination


class CatsListCreateView(generics.ListCreateAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyPagination


class CatsUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = [IsOwnerOrReadOnly]


class RatingsCreateView(generics.CreateAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cat_id = self.kwargs['pk']
        cat = Cats.objects.get(id=cat_id)
        rating, created = Ratings.objects.get_or_create(user=self.request.user, cat=cat)

        if created:
            serializer.save(cat=cat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            rating.rating = serializer.validated_data['rating']
            rating.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
