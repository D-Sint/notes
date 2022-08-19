from django.db import models
from django.utils import timezone as django_tz


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Note(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    text = models.TextField(max_length=5000)
    create_date = models.DateTimeField(default=django_tz.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
