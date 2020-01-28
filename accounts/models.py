from django.db import models

class Post(models.Model):

    username = models.CharField(max_length=20, blank=False,null=False)

    email = models.CharField(max_length=70)
    text = models.TextField(blank=False, null=False)


class Meta:
    db_table="post"

