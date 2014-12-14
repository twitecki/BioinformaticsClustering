from django.db import models

# Create your models here.

class KlusterUser(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.firstName + ' ' + self.lastName

class Kluster(models.Model):
	code = models.CharField(max_length=4)
	JSON = models.TextField()
	user = models.ForeignKey(KlusterUser)
	dateCreated = models.DateField(auto_now_add=True)
	timeCreated = models.TimeField(auto_now_add=True)

	def __unicode__(self):
		return self.code
