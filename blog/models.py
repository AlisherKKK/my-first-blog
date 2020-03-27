from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Person(models.Model):
	p_full_name = models.CharField("full_name", max_length=50)
	p_information = models.TextField("Information")
	p_date_birth = models.DateTimeField("published")

class Education(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	e_start = models.CharField("from", max_length=4)
	e_end = models.CharField("to", max_length=7)	
	e_place = models.CharField("Place", max_length=200)

class Experience(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	ed_start = models.CharField("from", max_length=4)
	ed_end = models.CharField("to", max_length=7)	
	ed_place = models.CharField("Place", max_length=200)

class Skills(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	s_name = models.CharField("from", max_length=15)
	s_percent = models.IntegerField()

	