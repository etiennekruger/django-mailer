from django.shortcuts import render, redirect
from django.db.models import F
from django.http import HttpResponse
from django.conf import settings
from os import path
from models import Message

def bug(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.get(pk=mid).view()
        except:
            pass
    location = path.join(settings.STATIC_ROOT, 'mailer', 'bug.png')
    file = open(location, 'rb')
    return HttpResponse(file.read(), mimetype='image/png')

def iframe(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.get(pk=mid).view()
        except:
            pass
    return HttpResponse('')

def click(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.get(pk=mid).view()
        except:
            pass
    url = request.GET.get('url', None)
    if url:
        return redirect(url)
    return HttpResponse(code=404)
