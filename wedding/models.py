from django.db import models

# Create your models here.
class Invitee(models.Model):
    party_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.party_name

class Invitee_extra(models.Model):
    invitee = models.ForeignKey(Invitee)
    guest = models.CharField(max_length=50)
    attend = models.IntegerField(default=0)
    test = models.CharField(max_length=50)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.invitee