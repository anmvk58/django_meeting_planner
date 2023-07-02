from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.
def welcome(request):
    # return HttpResponse("Welcome to the Meeting Planner!")
    meeting = Meeting.objects.all()
    return render(request, "website/welcome.html", {"meetings": meeting})