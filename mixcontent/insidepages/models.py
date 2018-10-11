from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class PostVer2(models.Model):
    title = models.CharField(max_length=120)
    counter = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    tagged_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.title


class VideoVer2(models.Model):
    ref_post = GenericRelation(PostVer2)
    ref_video = models.CharField(max_length=250)
    ref_subs = models.CharField(max_length=250)


class TextVer2(models.Model):
    full = models.TextField(default='-')
    short = models.CharField(max_length=100, default='-')
    ref_post = GenericRelation(PostVer2)


class AudioVer2(models.Model):
    bit_rate = models.CharField(max_length=50)
    ref_post = GenericRelation(PostVer2)


class MixPost(models.Model):
    title = models.CharField(max_length=120)
    counter = models.IntegerField(default=0)
    type_content = models.CharField(max_length=10)
    ref_content = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Page with posts"

    def __str__(self):
        return str(self.title) + '_' + str(self.type_content) + '_' + str(self.counter)


class Video(models.Model):
    parent = models.ForeignKey(MixPost, related_name='content', on_delete=models.CASCADE)
    ref_video = models.CharField(max_length=250)
    ref_subs = models.CharField(max_length=250)

    def __str__(self):
        return self.ref_video + '_' + self.ref_subs

    def __unicode__(self):
        return self.ref_video + '_' + self.ref_subs


class Audio(models.Model):
    parent = models.ForeignKey(MixPost, on_delete=models.CASCADE)
    bit_rate = models.CharField(max_length=50)

    def __str__(self):
        return self.bit_rate


class Texts(models.Model):
    parent = models.ForeignKey(MixPost, on_delete=models.CASCADE)
    TextDetail = models.CharField(max_length=250, null=True)
    FullText = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.TextDetail
