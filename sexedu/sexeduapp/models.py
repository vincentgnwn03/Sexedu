from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Laporan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama


from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/user1.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nama Kursus")
    description = models.TextField(verbose_name="Deskripsi Kursus")
    video = models.FileField(upload_to='videos/', verbose_name="Video Kursus", blank=True, null=True)
    ppt = models.FileField(upload_to='ppts/', verbose_name="PPT Kursus", blank=True, null=True)
    users = models.ManyToManyField(User, related_name='courses', verbose_name="Pengguna yang memiliki akses")

    def __str__(self):
        return self.name
