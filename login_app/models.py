from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # NAME_REGEX= re.compile(r'^[a-zA-z]+$')
        if len(post_data['first_name']) < 2 or len(post_data['first_name']) >50:
            errors['firstname']= "First name must be between 2 and 50 characters long"
        if len(post_data['last_name']) < 2 or len(post_data['last_name'])> 50:
            errors['lastname']= "Last name must be between 2 and 50 characters long"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address."
        check_email= User.objects.filter(email= post_data['email'])
        if check_email:
            errors['email_input']= "This email address already exists."
        if len(post_data['password']) < 8:
            errors['password']= "Password must be at least 8 characters long."
        if post_data['confirm_pw'] != post_data['password']:
            errors['confirm_pw']= "Passwords don't match."
        return errors

    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['log_email'] = "Invalid email address."
            return errors
        if len(post_data['password']) < 8:
            errors['password']= "Password must be at least 8 characters long."
        user= User.objects.filter(email=post_data['email'])
        if user:
            user= user[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors['log_password']= "Incorrect password."
        else:
            errors['log_email_password']= "Incorrect email."
        return errors


class User(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.CharField(max_length=100, unique=True)
    password= models.CharField(max_length=60)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects = UserManager()
