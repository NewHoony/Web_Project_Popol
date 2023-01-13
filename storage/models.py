from django.db import models
from main.models import User
from django.template.defaultfilters import slugify

class Project(models.Model):
    project = models.CharField(max_length=100)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploader", null=True, blank=True) 
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.project
    
    def summary(self):
        if len(self.content) > 30:
            return f"{self.content[:30]} ..."
        return self.content

class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to="File/%y/%m")
    con = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.project}_{self.con}'

# image file naming
# instance => 현재 정의된 모델의 인스턴스 
# filename => 파일에 원래 제공된 파일 이름. 이것은 최종 목적지 경로를 결정할 때 고려되거나 고려되지 않을 수 있음
    def get_image_filename(instance, file):
        # 해당 Post 모델의 title 을 가져옴
        title = instance.project.title
        # slug - 의미있는 url 사용을 위한 필드.
        # slugfy 를 사용해서 title을 slug 시켜줌.
        slug = slugify(title)
        # 제목 - 슬러그된 파일이름 형태
        return "Project_files/%s-%s" % (slug, file)  

# Create your models here.
