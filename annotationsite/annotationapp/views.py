from django.shortcuts import render
from .data import ANNOTATIONS
from django.http import Http404
# Create your views here.

def list(request):
    return render(request,"list.html")

def video(request):
    return render(request,"video.html", {})

def addAnnotation(request):

    if request.method=="POST" and request.user.is_authenticated:
        timestamp = request.POST.get('timestamp')
        annotation = request.POST.get('annotation')
        citation = request.POST.get('citation')

        ANNOTATIONS[len(ANNOTATIONS)] = {"timestamp":timestamp, "annotation":annotation, "citation":citation, "author": request.user.username}
        
    return render(request,"addAnnotation.html", {})

def index(request):
    return render(request,"index.html")

def viewAnnotation(request):
    # URL PARAMETERS ARE DEFAULT STRINGS
    id = int(request.GET.get("id", default=None))
    
    if id in ANNOTATIONS:
        return render(request,"viewAnnotation.html", {"id":id, "annotation":ANNOTATIONS[id]})
    else:
        raise Http404("The requested item cannot be found.")

def editAnnotation(request):
    id = int(request.GET.get("id", default=None))
    # URL PARAMETERS ARE DEFAULT STRINGS
    if request.method=="POST" and request.user.is_authenticated:
        timestamp = request.POST.get('timestamp')
        annotation = request.POST.get('annotation')
        citation = request.POST.get('citation')

        ANNOTATIONS[id] = {"timestamp":timestamp, "annotation":annotation, "citation":citation, "author": request.user.username}
        
    if id in ANNOTATIONS:
        return render(request,"editAnnotation.html", {"id":id, "annotation":ANNOTATIONS[id]})
    else:
        raise Http404("The requested item cannot be found.")
