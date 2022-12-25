from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class webPage(models.Model):
  judul = models.CharField(max_length=200)
  tipe = models.CharField(max_length=15)
  deskripsi = models.TextField()
  image = models.ImageField(null=True, blank=True, upload_to='images')
  video = models.FileField(null=True, blank=True, upload_to='videos', validators=[FileExtensionValidator(allowed_extensions=['ogg','mp4','webm'])])
  image_1 = models.ImageField(null=True, blank=True, upload_to='images')
  image_2 = models.ImageField(null=True, blank=True, upload_to='images')
  image_3 = models.ImageField(null=True, blank=True, upload_to='images')
  image_4 = models.ImageField(null=True, blank=True, upload_to='images')
  def __str__(self):
    return self.judul