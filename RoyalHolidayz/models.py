from django.db import models
from django.db.models import ManyToOneRel
class Candidate(models.Model):
	candidateid = models.AutoField(max_length = 6, primary_key = True)
	name = models.CharField(max_length = 20)
	
	def __unicode__(self):
		return u"%s %s"%(self.name, self.candidateid)

class Sponsorer(models.Model):
	LEGS_CHOICES = { ("L","Left"),("R","Right")}
	candidateid = models.ForeignKey(Candidate, primary_key = True,related_name="candidate")
	sponsorid = models.ForeignKey(Candidate)
	leg = models.CharField("Leg",max_length=1,choices=LEGS_CHOICES)
	
	def __unicode__(self):
		return u"%s, %s"%(self.candidateid, self.sponsorid)
