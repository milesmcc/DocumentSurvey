from django.db import models
import hashlib

class DocumentGroup(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Document(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    content = models.TextField()
    imprecise_views = models.IntegerField(default=0)

    @property
    def spid(self):
        return self.group.name[:5].replace(" ", "") + hashlib.md5(str(self.id).encode()).hexdigest()

class AccessKey(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    key = models.CharField(max_length=8, unique=True)
    imprecise_uses = models.IntegerField(default=0)

    def __str__(self):
        return self.key
