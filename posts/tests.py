from django.test import TestCase
from .models import Post, Tag
from django.utils import timezone
import datetime


# Create your tests here.
class PostTest(TestCase):

    def test_was_written_recently_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=1)
        post = Post(text='', pub_date=time)
        self.assertIs(post.was_written_recently(), False)

    def test_was_written_recently_with_old_post(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        post = Post(text='', pub_date=time)
        self.assertIs(post.was_written_recently(), False)

    def test_was_written_recently_with_new_post(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        post = Post(text='', pub_date=time)
        self.assertIs(post.was_written_recently(), True)

        
        