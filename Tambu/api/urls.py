from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('api/businesses/', views.getBusinesses, name='businesses'),
    path('api/businesses/<int:id>/', views.getBusiness, name='business'),
    path('api/businesses/<int:id>/reviews/', views.getReviews, name='business-reviews'),
    path('api/businesses/<int:id>/photos/', views.getPhotos, name='business-photos'),
    path('api/search/', views.searchBusinesses, name='search-businesses'),
]