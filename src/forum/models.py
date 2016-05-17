from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):

	CATEGORIES = (
		('Maurice', 'Maurice'),
		('France', 'France'),
		('Bachelorette', 'Bachelorette'),
		('Bachelor', 'Bachelor'),
		('Surpise Maries', 'Surprise-Maries')
	)

	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.CharField(max_length=100)
	category = models.CharField(max_length=50, choices=CATEGORIES ,blank=True)
	updated = models.DateTimeField(auto_now = True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("forum:detail", kwargs={"id" : self.id})


class Comment(models.Model) :
	post = models.ForeignKey('forum.Post', related_name='comments')
	author = models.CharField(max_length=100)
	text = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

