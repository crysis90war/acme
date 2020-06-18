from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampModel):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title