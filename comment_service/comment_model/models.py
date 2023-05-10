from __future__ import unicode_literals
from django.db import models
from datetime import date

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

# Create your models here.
class comment_Model(models.Model):
    content = models.CharField(max_length=50)
    userId = models.CharField(max_length=50)
    userName = models.CharField(max_length=12)
    dateComment = CustomDateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.content, self.userId, self.userName, self.dateComment)
    
