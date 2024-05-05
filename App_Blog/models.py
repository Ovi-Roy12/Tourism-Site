from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=264, verbose_name='Put on a Title')
    blog_content = models.TextField(verbose_name='what is on your mind')
    blog_image = models.ImageField(upload_to='blog_images',verbose_name='Image')
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-publish_date',]
    def __str__(self):
        return self.blog_title
