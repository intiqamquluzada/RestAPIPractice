from django.db import models


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(editable=False, unique=True, )

    class Meta:
        abstract = True
