from django.db import models

# database for users
class User(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    image = models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')

    def __str__(self):
        return self.firstname

    def __unicode__(self):
        return self.firstname
