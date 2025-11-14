from django.db import models

from book.app.Domain.value_objects import Slug


class Cycle(models.Model):
    title = models.CharField(blank=False, null=False, unique=True)
    slug = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = Slug.format_str(self.title)
        super().save(*args, **kwargs)
