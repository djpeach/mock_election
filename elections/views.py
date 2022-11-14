from django.shortcuts import render


def results(request):
    return render(request, "elections/results.html")


def vote(request):
    return render(request, "elections/vote.html")
