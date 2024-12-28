from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/")
    github_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text='Enter percentage (0-100')

    def __str__(self):
        return self.name
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    desigination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name