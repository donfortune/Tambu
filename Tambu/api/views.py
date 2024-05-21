from django.shortcuts import render
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/businesses/',
            'method': 'GET',
            'description': 'Returns an array of businesses'
        },
        {
            'Endpoint': '/api/businesses/id',
            'method': 'GET',
            'description': 'Returns a single business object'
        },
        {
            'Endpoint': '/api/businesses/id/reviews',
            'method': 'GET',
            'description': 'Returns all reviews for a business'
        },
        {
            'Endpoint': '/api/businesses/id/photos',
            'method': 'GET',
            'description': 'Returns all photos for a business'
        },
        {
            'Endpoint': '/api/businesses/search',
            'method': 'GET',
            'description': 'Returns businesses based on a search term'
        },
        {
            'Endpoint': '/api/businesses/id/photos',
            'method': 'POST',
            'description': 'Upload a photo to a business'
        },
        {
            'Endpoint': '/api/reviews/',
            'method': 'POST',
            'description': 'Create a new review'
        },
        {
            'Endpoint': '/api/reviews/id',
            'method': 'PUT',
            'description': 'Update a review'
        },
        {
            'Endpoint': '/api/reviews/id',
            'method': 'DELETE',
            'description': 'Delete a review'
        },
        {
            'Endpoint': '/api/users/id',
            'method': 'GET',
            'description': 'Returns a single user object'
        },
        {
            'Endpoint': '/api/users/id',
            'method': 'PUT',
            'description': 'Update a user'
        },
        {
            'Endpoint': '/api/users/id',
            'method': 'DELETE',
            'description': 'Delete a user'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getBusinesses(request):
    businesses = Business.objects.all()
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBusiness(request, id):
    business = Business.objects.get(id=id)
    serializer = BusinessSerializer(business, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getReviews(request, id):
    #business = Business.objects.get(Business, id=id)
    reviews = Review.objects.get(id=id)
    serializer = ReviewSerializer(reviews, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPhotos(request, id):
    photos = Photo.objects.get(id=id)
    serializer = PhotoSerializer(photos, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def searchBusinesses(request):
    query = request.query_params.get('keyword', '')
    businesses = Business.objects.filter(name__icontains=query)
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)