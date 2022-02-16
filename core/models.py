from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }

class Event(models.Model):
    description = models.CharField(max_length=1024)
    source = models.CharField(max_length=512)
    age = models.IntegerField()
    sourceAge = models.CharField(max_length=512)

    def update_from_dict(self, d):
        self.description = d['description']
        self.source = d['source']
        self.age = d['age']
        self.sourceAge = d['sourceAge']
        self.save()

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'source': self.source,
            'age': self.age,
            'sourceAge': self.sourceAge
        }

    class Meta:
        ordering = ('id',)
