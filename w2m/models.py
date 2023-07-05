from django.db import models
from random import randint


def random_code():
    return str(randint(0, 99999999)).zfill(8)


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    pw = models.CharField(max_length=255)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to="user_images/", blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    belonging_groups = models.ManyToManyField(to="Group", blank=True)

    def save(self, *args, **kwargs):
        if self.img:
            self.img_path = self.img.url
        super().save(*args, **kwargs)


class Group(models.Model):
    group_name = models.CharField(max_length=50, default="New Group")
    group_code = models.CharField(max_length=8, primary_key=True, default=random_code)
    group_users = models.ManyToManyField(User)
