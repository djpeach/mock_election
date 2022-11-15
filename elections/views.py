from django.shortcuts import render, redirect
from .models import *


def results(request):
    election = Election.objects.get(pk=1)
    ctx = {
        "election": election,
    }
    return render(request, "elections/results.html", ctx)


def vote(request):
    if request.method == "POST":
        print(request.POST)
        raceIds = request.POST["raceIds"].split(',')[:-1]
        voter = Voter.objects.get(pk=request.POST["voterId"])
        for raceId in raceIds:
            race = Race.objects.get(pk=raceId)
            selected_candidate_id = request.POST[f"candidateIdRace{raceId}"]
            candidate = Candidate.objects.get(pk=selected_candidate_id)
            session_id = request.session
            Vote.objects.create(
                voter=voter,
                race=race,
                candidate=candidate,
                session_id=session_id
            )
        return redirect("results")

    races = Race.objects.filter(election=1)
    voters = Voter.objects.all()
    ctx = {
        "voters": voters,
        "races": races,
    }
    return render(request, "elections/vote.html", ctx)
