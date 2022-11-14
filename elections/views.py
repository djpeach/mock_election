from django.shortcuts import render
from .models import *


def results(request):
    election = Election.objects.get(pk=1)
    ctx = {
        "election": election,
    }
    return render(request, "elections/results.html", ctx)


def vote(request):
    races = Race.objects.filter(election=1)
    voters = Voter.objects.all()
    ctx = {
        "voters": voters,
        "races": races,
    }
    return render(request, "elections/vote.html", ctx)
