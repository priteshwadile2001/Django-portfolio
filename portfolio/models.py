from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(null=True)
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    authname = models.CharField(max_length=15)
    # sql lite does not store the imgaes it only store description and text for that we have to create a media folder to store the image
    # upload_to=blog = it will create automatic a blog folder 
    # blank=True : if image can't upload its fine it will handal
    # null= True : it will handle null value also , it nothing is there its okay
    img =  models.ImageField(upload_to='bolg',blank=True,null=True)
    # The date will added automatic
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title