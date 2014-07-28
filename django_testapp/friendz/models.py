from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
  fromUser = models.ForeignKey(User, related_name="fromUser")
  toUser = models.ForeignKey(User, related_name="toUser")
  dateAdded = models.DateField()
  unique_together = ("fromUser", "toUser")

  def save(self, *args, **kwargs):
    if self.fromUser == self.toUser:
      return
    else:
      super(UserLink, self).save(*args, **kwargs)

  def __unicode__(self):
    return self.fromUser.username+" is following "+self.toUser.username