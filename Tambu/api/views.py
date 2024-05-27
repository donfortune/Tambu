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

@api_view(['POST'])
def createBusiness(request):
    data = request.data
    owner = User.objects.get(id=data['owner'])
    category = Category.objects.get(id=data['category'])
    business = Business.objects.create(
        name=data['name'],
        owner=owner,
        category=category,
        description=data['description'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        country=data['country'],
        postal_code=data['postal_code'],
        phone_number=data['phone_number'],
        website=data['website']
    )
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

@api_view(['POST'])
def uploadPhoto(request, id):
    business = Business.objects.get(id=id)
    photo = request.data['photo']
    photo = Photo.objects.create(
        business=business,
        image=photo
    )
    serializer = PhotoSerializer(photo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createReview(request):
    data = request.data
    business = Business.objects.get(id=data['business'])
    user = User.objects.get(id=data['user'])
    review = Review.objects.create(
        user=user,
        business=business,
        rating=data['rating'],
        title=data['title'],
        body=data['body']
    )
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)
    

@api_view(['PUT'])
def updateReview(request, id):
    review = Review.objects.get(id=id)
    data = request.data
    review.rating = data['rating']
    review.title = data['title']
    review.body = data['body']
    review.save()
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteReview(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return Response('Review deleted successfully')


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, id):
    user = User.objects.get(id=id)
    serializers = UserSerializer(user, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getUserReview(request, id):
    user = User.objects.get(id=id)
    reviews = user.reviews.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserPhoto(request, id):
    user = User.objects.get(id=id)
    photos = user.photos.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBusinessCategory(request, id):
    business = Business.objects.get(id=id)
    category = business.category
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getBusinessInCategory(request, id):
    category = Category.objects.get(id=id)
    businesses = category.businesses.all()
    serializer = BusinessSerializer(businesses, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def updateBusiness(request, id):
    business = Business.objects.get(id=id)
    data = request.data
    business.name = data['name']
    business.description = data['description']
    business.address = data['address']
    business.city = data['city']
    business.state = data['state']
    business.country = data['country']
    business.postal_code = data['postal_code']
    business.phone_number = data['phone_number']
    business.website = data['website']
    business.save()
    serializer = BusinessSerializer(business, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def recentReviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    #business = Business.objects.get(id=id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)



