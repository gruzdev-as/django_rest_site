from django.db import models


class Tag(models.Model):
    '''Describe a tag for any post''' 

    name = models.CharField(
        max_length = 20,
        verbose_name = 'Name',
        unique = True,
        )

    class Meta:

        verbose_name_plural = 'Tags'

    def __str__(self):

        return self.name

class Post(models.Model):
    '''Describe a post in the feed'''

    name = models.CharField( 
        max_length = 50,
        verbose_name = 'Name',
        db_index = True,
        )
    description = models.CharField(
        max_length = 200,
        verbose_name = 'Description',
        )
    date_added = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Date added',
        )
    tag = models.ManyToManyField(
        Tag,
        verbose_name = 'Tags',
        )
    image = models.ImageField(
        upload_to = 'uploads/',
        verbose_name = 'Image',
        )

    def __str__(self):

        return self.name


