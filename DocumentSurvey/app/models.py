from django.db import models
import hashlib
from .cleaner import clean_text

class DocumentGroup(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Document(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    content = models.TextField()
    imprecise_views = models.IntegerField(default=0)
    dynamic_cleaning = models.BooleanField(default=True)

    @property
    def spid(self):
        return str(self.id) + self.group.name[:5].replace(" ", "") + hashlib.md5(str(self.id).encode()).hexdigest()

    @property
    def display_format(self):
        if self.dynamic_cleaning:
            return clean_text(self.content)
        return self.content

class AccessKey(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    key = models.CharField(max_length=8, unique=True)
    imprecise_uses = models.IntegerField(default=0)

    def __str__(self):
        return self.key
