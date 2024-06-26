from django.db import models


# Create your models here.
class Campaign(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField (auto_now_add= True)
    updedted = models.DateTimeField (auto_now = True)
    logo = CloudinaryFile('Image' ,overwrite= True ,format = "jpg")
  
    class Meta:
        orderting = (' -created-at')

    def __str__(self):
        return self.title   
    


    





