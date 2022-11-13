from django.contrib import admin
from .models import *
from .forms import *


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    form = ElectionAdminForm


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    form = RaceAdminForm


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateAdminForm


@admin.register(RunningMate)
class RunningMateAdmin(admin.ModelAdmin):
    form = RunningMateAdminForm


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    form = VoterAdminForm


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    form = VoteAdminForm
