#from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(models.Model):
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='businesses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='businesses')
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Nigeria')
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'business')

    def __str__(self):
        return f"{self.user.username} - {self.business.name}"

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='photos', blank=True, null=True)
    image = models.ImageField(upload_to='business_photos/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo by {self.user.username}"

class BusinessHours(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='hours')
    day_of_week = models.PositiveSmallIntegerField(choices=[
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')
    ])
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        unique_together = ('business', 'day_of_week')

    def __str__(self):
        return f"{self.business.name} Hours"
