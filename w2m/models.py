from django.db import models
from random import randint
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = BASE_PATH[: BASE_PATH.find("w2m") - 1]


def random_code():
    return str(randint(0, 99999999)).zfill(8)


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    pw = models.CharField(max_length=255)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to="", blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)
    belonging_groups = models.ManyToManyField(to="Group", blank=True)
    my_unavailable_datetimes = models.JSONField(blank=True, default=dict)

    def save(self, *args, **kwargs):
        try:
            mode = args[0]
            if mode == "create_group":
                super().save((), **kwargs)
                return
            elif mode == "update_group":
                super().save((), **kwargs)
                return
            elif mode == "exit_group":
                super().save((), **kwargs)
                return
            elif mode == "add_my_time_table":
                super().save((), **kwargs)
                return
        except:
            if self.img:
                file_type = self.img.url[self.img.url.index(".") + 1 :]
                new_img_path = "/media/%s.%s" % (self.id, file_type)
                self.img_path = new_img_path
                super().save(*args, **kwargs)
                with open(BASE_PATH + self.img.url, mode="rb") as f:
                    all_data = f.read()
                    with open(BASE_PATH + new_img_path, mode="wb") as g:
                        g.write(all_data)
            if self.img:
                os.remove(BASE_PATH + self.img.url)
                return
        super().save(*args, **kwargs)


class Group(models.Model):
    group_name = models.CharField(max_length=50, default="New Group")
    group_code = models.CharField(max_length=8, primary_key=True, default=random_code)
    group_users = models.ManyToManyField(User)
    group_unavailable_datetimes = models.JSONField(blank=True, default=dict)
