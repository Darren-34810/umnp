from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class webPage(models.Model):
  judul = models.CharField(max_length=200)
  tipe = models.CharField(max_length=15)
  deskripsi = models.TextField()
  image = models.ImageField(null=True, blank=True, upload_to='images')  
  video = models.FileField(null=True, blank=True, upload_to='videos', validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

  def __str__(self):
    return self.judul