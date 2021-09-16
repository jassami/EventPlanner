from planner.models import Event, Comment
from django.shortcuts import redirect, render
from login_app.models import User
import folium
import geocoder

def home(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    context= {
        'events': Event.objects.all(),
    }
    return render(request, 'home.html', context)

def add_event(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    request.session['title']= request.POST['title']
    request.session['description']= request.POST['description']
    request.session['location']= request.POST['location']
    request.session['date_time']= request.POST['date_time']
    user= User.objects.get(id= request.session['user_id'])
    Event.objects.create(title= request.session['title'], description= request.session['description'], location= request.session['location'], creator= user, date_time= request.session['date_time'])
    return redirect('/events')

def event(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    event= Event.objects.get(id= event_id)
    place= event.location
    location= geocoder.osm(place)
    lat= location.lat
    lng= location.lng
    country= location.country
    #  create map object
    m = folium.Map(location=[19,-12], zoom_start=3)
    # folium.Marker([5.5, -1], tooltip= 'Click for more', popup='place').add_to(m)
    folium.Marker([lat, lng], tooltip= 'Click for more', popup=country).add_to(m)
    #  Get HTML representation of map object
    m = m._repr_html_()
    context={
        'event': event,
        'comments': Comment.objects.filter(event= event),
        'm':m,
    }
    return render(request, 'event.html', context)

def add_comment(request, event_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    event= Event.objects.get(id= event_id)
    user= User.objects.get(id= request.session['user_id'])
    Comment.objects.create(post= request.POST['post'], user= user, event= event)
    return redirect(f'/events/event/{event.id}')

