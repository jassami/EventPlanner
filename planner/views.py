from planner.models import Event, Comment
from django.shortcuts import redirect, render
from login_app.models import User

def home(request):
    context= {
        'events': Event.objects.all(),
    }
    return render(request, 'home.html', context)

def add_event(request):
    request.session['title']= request.POST['title']
    request.session['description']= request.POST['description']
    request.session['location']= request.POST['location']
    request.session['date_time']= request.POST['date_time']
    user= User.objects.get(id= request.session['user_id'])
    event= Event.objects.create(title= request.session['title'], description= request.session['description'], location= request.session['location'], creator= user, date_time= request.session['date_time'])
    return redirect('/events')

def event(request, event_id):
    event= Event.objects.get(id= event_id)
    context={
        'event': event,
        'comments': Comment.objects.filter(event_comment= event)
    }
    return render(request, 'event.html', context)

def add_comment(request, event_id):
    event= Event.objects.get(id= event_id)
    user= User.objects.get(id= request.session['user_id'])
    Comment.objects.create(post= request.POST['post'], poster= user, event_comment= event)
    return redirect('/events/event')

