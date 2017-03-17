from django.db import models

class Course(models.Model):

    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Shortcut')
    description = models.TextField('Description', blank=True)
    start_date = models.DateField('Start Date', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Image', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
# Create your models here.
