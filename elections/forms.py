from django import forms

from .models import *


class ElectionAdminForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"
        widgets = {"name": forms.TextInput}


class RaceAdminForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = "__all__"
        widgets = {"name": forms.TextInput}


class CandidateAdminForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"
        widgets = {"name": forms.TextInput}


class RunningMateAdminForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"
        widgets = {"name": forms.TextInput}


class VoterAdminForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"
        widgets = {"name": forms.TextInput}


class VoteAdminForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = "__all__"
