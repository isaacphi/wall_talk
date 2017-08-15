from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField()

    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.text