from django.db import models
from django.urls import reverse
from book.app.Domain.value_objects import Slug


class Category(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category.index', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)
