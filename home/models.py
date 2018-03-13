from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class post(models.Model):
    post_title = models.CharField('Title', max_length = 50, unique = True)
    post_text = models.CharField('Text', max_length = 5000)
    pub_date = models.DateTimeField('Date Published')
    likes = models.IntegerField('Likes', default = 0 )

    def __str__(self):
        self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
