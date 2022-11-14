from django.db import models


class Election(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.TextField()
    election = models.ForeignKey("Election", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    class PartyEnum(models.TextChoices):
        REPUBLICAN = "REPUBLICAN", "Republican"
        DEMOCRAT = "DEMOCRAT", "Democrat"

    race = models.ForeignKey("Race", on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    name = models.TextField()
    running_mate = models.OneToOneField("RunningMate", on_delete=models.PROTECT)
    party = models.TextField(choices=PartyEnum.choices)

    @property
    def bootstrap_party_color(self):
        if self.party == self.PartyEnum.REPUBLICAN:
            return 'danger'
        elif self.party == self.PartyEnum.DEMOCRAT:
            return 'primary'
        else:
            return 'secondary'

    def __str__(self):
        return self.name


class RunningMate(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Voter(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    race = models.ForeignKey("Race", on_delete=models.CASCADE)
    voter = models.ForeignKey("Voter", on_delete=models.CASCADE)
    candidate = models.ForeignKey("Candidate", on_delete=models.CASCADE)
    session_id = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.race.name}: {self.voter.name} - {self.candidate.name}"
