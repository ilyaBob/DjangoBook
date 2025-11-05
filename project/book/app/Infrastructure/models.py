from django.db import models
from django.urls import reverse


class Author(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)


class Reader(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)
    description = models.TextField(max_length=4000, blank=False, null=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField(blank=False, null=False)
    time = models.CharField(blank=False, null=False)

    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    reader = models.ForeignKey(
        'Reader',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    published = PublishedManager()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('book__show', kwargs={'slug': self.slug})


