from django.db import models
import uuid
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	thumbnail = models.ImageField(null=True)
	tag = models.CharField(max_length=200, null=True, blank=True)
	body = RichTextUploadingField()
	slug = models.SlugField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	# generating random object of 28bits
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)


	def __str__(self):
		return self.title

class Comment(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

class Skill(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(default='/images/download.jpg', null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
	def __str__(self):
		return self.title
		
class Tag(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	id  = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.name


class Message(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=50)
	body = models.TextField()
	is_read = models.BooleanField(default=False, null=True, blank=True)
	subject = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

	def __str__(self):
		return self.name[0:20]

class Endorsements(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField(null=True, blank=True)
	featured = models.BooleanField(default=False)
	approved = models.BooleanField(default=False, null=True)
	featured = models.BooleanField(default=False)

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

	
	def __str__(self):
		return self.name

class Questions(models.Model):
	TYPES = (
		('frontend', 'frontend'),
		('backend', 'backend'),
		('fullstack','fullstack'),
	)

	answer = models.CharField(max_length=200, choices=TYPES)
	created  =  models.DateTimeField(auto_now_add=True)
	id  = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False )