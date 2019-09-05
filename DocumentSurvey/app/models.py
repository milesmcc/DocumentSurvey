from django.db import models

class DocumentGroup(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Document(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    content = models.TextField()
    imprecise_views = models.IntegerField(default=0)

class AccessKey(models.Model):
    group = models.ForeignKey(DocumentGroup, on_delete=models.CASCADE)
    key = models.CharField(max_length=8, unique=True)
    imprecise_uses = models.IntegerField(default=0)

    def __str__(self):
        return self.key
