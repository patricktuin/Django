from django.db import models

# Create your models here.
class Invitee(models.Model):
    invitee = models.CharField(max_length=50)
    attend = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Invitee_extra(models.Model):
    invitee = models.ForeignKey(Invitee)
    invitee_extra = models.CharField(max_length=50)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.ingredient

