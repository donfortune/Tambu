from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('api/businesses/', views.getBusinesses, name='businesses'),
    path('api/businesses/<int:id>/', views.getBusiness, name='get-business'),
    path('api/businesses/<int:id>/categories/', views.getBusinessInCategory, name='create-category'),
    path('api/businesses/create/', views.createBusiness, name='create-business'),
    path('api/businesses/<int:id>/update/', views.updateBusiness, name='update-business'),
    path('api/businesses/<int:id>/reviews/', views.getReviews, name='business-reviews'),
    path('api/businesses/<int:id>/upload/', views.uploadPhoto, name='upload-photo'),
    path('api/businesses/<int:id>/photos/', views.getPhotos, name='business-photos'),

    path('api/categories/', views.getCategories, name='get - categories'),
    path('api/categories/<int:id>/', views.getBusinessCategory, name='category'),

    path('api/search/', views.searchBusinesses, name='search-businesses'),
    
    path('api/reviews/create/', views.createReview, name='create-review'),
    path('api/reviews/<int:id>/update/', views.updateReview, name='update-review'),
    path('api/reviews/<int:id>/delete/', views.deleteReview, name='delete-review'),


    path('api/users/', views.getUsers, name='users'),
    path('api/users/<int:id>/', views.getUser, name='user'),
    path('api/users/<int:id>/reviews/', views.getUserReview, name='user-review'),
    path('api/users/<int:id>/photos/', views.getUserPhoto, name='user-photo'),
    
]