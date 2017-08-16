from django.db import models
from django.utils import timezone
import datetime


class Tag(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag, blank=True)

    def was_written_recently(self):
        # make sure the post isn't in the future
        if self.pub_date > timezone.now():
            return False
        else:
            return (timezone.now() - self.pub_date) < datetime.timedelta(days=1)

    def __str__(self):
        return self.text