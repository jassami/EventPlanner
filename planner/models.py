from django.db import models
from login_app.models import User

class Event(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField()
    creator= models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    date_time= models.DateTimeField(auto_now_add=True)
    location= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post= models.TextField()
    poster= models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    event_comment= models.ForeignKey(Event, related_name="event_comments", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
