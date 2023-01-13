from django.db import models
from main.models import User
# Create your models here.


class Project(models.Model):
    project = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bprojcet_maker", null=True, blank=True) 
    content = models.TextField()
    tech = models.TextField()
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.project
    
    def summary(self):
        if len(self.content) > 50:
            return f"{self.content[:50]} ..."
        return self.content

    def summary2(self):
        if len(self.project) > 30:
            return f"{self.project[:30]} ..."
        return self.project

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="bproject/%y/%m")
    con = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.project}_{self.con}"