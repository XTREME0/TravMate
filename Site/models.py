from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want for the user profile

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    city = models.CharField(max_length=100)  # Add city field
    travel_date = models.DateField()  # Add travel_date field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    # Add any additional fields you want for the user profile

    def __str__(self):
        return self.user.username