from django.db import models
from taggit.models import Tag
from taggit.managers import TaggableManager


class Photo(models.Model):
    """
    Model of photos
    """
    src = models.CharField(max_length=50)
    user_id = models.PositiveIntegerField()
    created = models.DateTimeField()
    likes = models.PositiveIntegerField()

    tags = TaggableManager()


class Tagstate(models.Model):
    """
    Tag state model
    """
    tag = models.ForeignKey(Tag, related_name='tag_state',)
    state = models.PositiveSmallIntegerField(
        default=0,
        choices=((0, 'Published'), (1, 'Hidden')), )
