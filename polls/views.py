# Create your views here.
from django.shortcuts import render_to_response
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    return render_to_response('polls/detail.html', {'poll_id': poll_id})

def results(request, poll_id):
    return render_to_response('polls/results.html', {'poll_id': poll_id})

def vote(request, poll_id):
    return render_to_response('polls/vote.html', {'poll_id': poll_id})
