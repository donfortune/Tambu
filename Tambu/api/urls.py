from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('api/businesses/', views.getBusinesses, name='businesses'),
    path('api/businesses/<int:id>/', views.getBusiness, name='business'),
    path('api/businesses/<int:id>/reviews/', views.getReviews, name='business-reviews'),
    path('api/businesses/<int:id>/photos/', views.getPhotos, name='business-photos'),
    path('api/search/', views.searchBusinesses, name='search-businesses'),
    path('api/businesses/<int:id>/upload/', views.uploadPhoto, name='upload-photo'),
    path('api/reviews/create/', views.createReview, name='create-review'),
    path('api/reviews/<int:id>/update/', views.updateReview, name='update-review'),
    path('api/reviews/<int:id>/delete/', views.deleteReview, name='delete-review'),
    path('api/users/', views.getUsers, name='users'),
    path('api/users/<int:id>/', views.getUser, name='user'),
    
    
]