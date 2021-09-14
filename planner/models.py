from django.db import models
from django.db.models.fields import TextField
from login_app.models import User

class Event(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField()
    creator= models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    event_date_time= models.DateTimeField(auto_now_add=True)
    event_location= models.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

