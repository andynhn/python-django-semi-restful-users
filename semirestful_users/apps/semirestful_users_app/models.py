from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name is required"
        elif len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name is required"
        elif len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        if len(postData['email']) < 1:
            errors["email"] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid Email Address"
        if User.objects.filter(email = postData['email']):
            errors["email"] = "Sorry, email is already in use"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User: {self.id} {self.name} {self.email}>"
    
    objects = UserManager()
