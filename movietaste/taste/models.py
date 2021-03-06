from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('taste:movie_in_category', args=[self.slug])

class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='movies')
    category_name = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='movies/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    review = models.TextField(blank=True)
    director = models.TextField(blank=True)
    rating = models.TextField(blank=True)
    open_date = models.TextField(blank=True)
    youtube = models.URLField(blank=True)
    available_display = models.BooleanField('Display', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('taste:movie_detail', args=[self.id, self.slug])

