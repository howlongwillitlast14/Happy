from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
##return the path 

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
	#the FileField knows that if the upload_to to the method, 
	# it should pass in an instance from django and filename

	def __str__(self):
		return self.title

