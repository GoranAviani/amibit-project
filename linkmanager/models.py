from django.db import models

# Create your models here.

class Link(models.Model):
    link_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    link_name = models.CharField(max_length=200)
    link_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_name

class Note(models.Model):
	note_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	note_title = models.CharField(max_length=200)
	note_text = models.TextField()
	note_timestamp = models.DateTimeField(auto_now_add=True) #auto_now_add time the instance was created
	note_slug = models.SlugField(max_length=250)

	def __str__(self):
		return self.note_title
