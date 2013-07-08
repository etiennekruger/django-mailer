from django.shortcuts import render, redirect
from django.db.models import F
from django.http import HttpResponse
from models import Message

def bug(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.filter(pk=mid).update(views=F('views')+1)
        except:
            pass
    return render(request, 'mailer/bug.png', {}, mimetype='image/png')

def iframe(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.filter(pk=mid).update(views=F('views')+1)
        except:
            pass
    return HttpResponse('')

def click(request):
    mid = request.GET.get('mid', None)
    if mid:
        try:
            Message.objects.filter(pk=mid).update(clicks=F('clicks')+1)
        except:
            pass
    url = request.GET.get('url', None)
    if url:
        return redirect(url)
    return HttpResponse(code=404)
