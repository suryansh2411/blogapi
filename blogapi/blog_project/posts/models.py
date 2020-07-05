from django.db import models
from django.conf import settings
from django.utils import timezone 

User = settings.AUTH_USER_MODEL

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(blank=True, null=True)


class Author(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField()
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title
		return self.username

	def publish(self):
		self.published_date = timezone.now()
	
# Create your models here.
