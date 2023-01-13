from django.db import models
from main.models import User

class Note(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")  # 글 쓴사람을 1:n관계로
    content = models.TextField()
    pubdate = models.DateTimeField() # DateTimeField로 최신 글을 가장 위로 
    likey = models.ManyToManyField(User, blank=True, related_name="likey") # 투표 기능 활성화

    def __str__(self):
        return self.subject

    def summary(self):          # board의 글이 너무 길면 50자 안으로 축약해서 출력
        if len(self.content) > 50:
            return f"{self.content[:50]}..."
        return self.content

    def hot(self):              # 좋아요 기능 추가
        if self.likey.count() >= 2:
            return True
        return False

class Reply(models.Model):
    board = models.ForeignKey(Note, on_delete= models.CASCADE)
    replyer = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.board}_{self.replyer}"


