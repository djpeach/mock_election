import socket

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *


def results(request):
    election = Election.objects.get(pk=1)
    ctx = {
        "election": election,
    }
    return render(request, "elections/results.html", ctx)


def vote(request):
    print(request.get_host())
    election = Election.objects.get(pk=1)
    races = Race.objects.filter(election=1)
    voters = Voter.objects.all()
    ctx = {
        "voters": voters,
        "races": races,
    }
    if request.method == "POST":
        if not election.is_active:
            ctx["error"] = f"The {election.name} is not yet active"
            ctx["error_level"] = "warning"
            return render(request, "elections/vote.html", ctx)
        raceIds = request.POST["raceIds"].split(",")[:-1]
        voter = Voter.objects.get(pk=request.POST["voterId"])
        if voter.vote_set.count() > 0:
            ctx[
                "error"
            ] = f"You have already voted. If you believe this is an error, please contact the teacher"
            ctx["error_level"] = "warning"
            return render(request, "elections/vote.html", ctx)
        for raceId in raceIds:
            race = Race.objects.get(pk=raceId)
            selected_candidate_id = request.POST[f"candidateIdRace{raceId}"]
            candidate = Candidate.objects.get(pk=selected_candidate_id)
            if not request.session.session_key:
                request.session.save()
            session_id = request.session.session_key
            session_votes = Vote.objects.filter(session_id=session_id, race_id=raceId)
            if session_votes.count() > 0:
                previous_vote = session_votes.first()
                send_mail(
                    "Voter Fraud Detected",
                    f"A session previously used to cast this vote: {request.get_host()}/admin/elections/vote/{previous_vote.id}/change/ was used to try to cast a vote for {candidate.name} in {race.name} by {voter.name}. Most likely either {previous_vote.voter.name} is attempting to vote on others' behalf. Best to delete the previous vote, and inform both voters what occurred.",
                    "dpeachesdev@gmail.com",
                    ["peachgarrett05@gmail.com"],
                    fail_silently=False,
                )
                ctx["error"] = (
                    f"Voter fraud detected. Admin has been notified. "
                    f"If you believe this is an error, please contact the teacher"
                )
                ctx["error_level"] = "danger"

                return render(request, "elections/vote.html", ctx)
            Vote.objects.create(
                voter=voter, race=race, candidate=candidate, session_id=session_id
            )
        return redirect("results")
    return render(request, "elections/vote.html", ctx)
