from django.db import models
from django.urls import reverse
from ..Domain.value_objects import Slug


class Author(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)


class Reader(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)


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
    cycle_number = models.IntegerField(blank=True, null=True)

    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    cycle = models.ForeignKey(
        'Cycle',
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

    category = models.ManyToManyField('Category', related_name='books', blank=True)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book__show', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)


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


class Cycle(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)
