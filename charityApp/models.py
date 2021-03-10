from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class AboutUS(models.Model):
	about_title = models.CharField(max_length=200, null=True)
	about_shortDes = models.TextField(null=True)
	about_detail = models.TextField(null=True)

	def __str__(self):
		return self.about_title

class Project(models.Model):
	pro_name = models.CharField(max_length=200)
	pro_image = models.ImageField(upload_to='images/', null=True)
	pro_detail = models.TextField(null=True)
	pro_date = models.DateTimeField(null=True, blank=True)


	def __str__(self):
		return self.pro_name

class ExecutiveMember(models.Model):
	ex_name = models.CharField(max_length=200)
	ex_image = models.ImageField(upload_to='images/', null=True)
	ex_designation = models.CharField(max_length=120, null=True, blank=True)
	ex_detail = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.ex_name

class Members(models.Model):
	mem_name = models.CharField(max_length=120)
	mem_email = models.EmailField(  null=True)
	mem_contact = models.CharField(max_length=200, null=True)
	mem_image = models.ImageField(upload_to='images/', null=True)
	mem_address = models.CharField(max_length=250, null=True)
	mem_details = models.TextField(null=True, blank=True)
	mem_joinDate = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.mem_name

class Contact(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.EmailField()
	user_contact = models.CharField(max_length=120)
	message = models.TextField()

	def __str__(self):
		return self.first_name


class Events(models.Model):
	event_name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, null=True)
	event_desc = models.TextField()
	event_image = models.ImageField(upload_to='images/', null=True, blank=True)
	event_location = models.CharField(max_length=120)
	event_date = models.DateField()
	event_time = models.CharField(max_length=80, null=True)

	def __str__(self):
		return self.event_name

	class Meta:
		ordering=('event_name',)
		index_together=(('id', 'slug'),)

	def get_absolute_url(self):
		return reverse('event_detail', args=[self.id, self.slug])


class SuccessStory(models.Model):
	story_title = models.CharField(max_length=200)
	story_image = models.ImageField(upload_to='images/')
	story_details = models.TextField()

	def __str__(self):
		return self.story_title

class ImageGallery(models.Model):
	gellery_title = models.CharField(max_length=120, null=True, blank=True)
	gellery_image = models.ImageField(upload_to='images/')
	gellery_detail = models.TextField(null=True, blank=True)


	def __str__(self):
		return self.gellery_title

class VideoGallery(models.Model):
	video_title = models.CharField(max_length=200, blank=True, null=True)
	video_gallery = models.FileField(upload_to='videos/', null=True, blank=True)

	def __str__(self):
		return self.video_title

class Terms(models.Model):
	term_title = models.CharField(max_length=200)
	term_desc = models.TextField()

	def __str__(self):
		return self.term_title





