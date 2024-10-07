from django.urls import path

from .views import CatsListCreateView, CatsUpdateDestroyView, BreedListCreateView, RatingsCreateView

urlpatterns = [
    path('cats/', CatsListCreateView.as_view(), name='cats-list-create'),
    path('cats/<int:pk>/', CatsUpdateDestroyView.as_view(), name='cat-detail'),
    path('breeds/', BreedListCreateView.as_view(), name='breeds-list'),
    path('cats/<int:pk>/ratings/', RatingsCreateView.as_view(), name='rating-create'),
]
