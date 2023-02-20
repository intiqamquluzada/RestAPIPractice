from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from services.uploader import Uploader


class Post(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    image = models.ImageField(upload_to=Uploader.upload_images, blank=True, null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="modified_by")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Post)
        super(Post, self).save(*args, **kwargs)
