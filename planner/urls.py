from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('add_event', views.add_event),
    path('event/<int:event_id>', views.event),
    path('add_comment/<int:event_id>', views.add_comment),
]
