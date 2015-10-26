from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from rest_framework.authtoken.models import Token
from jsonfield import JSONField


class Org(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=254, null=True, blank=True, unique=True)
    
    attrs = JSONField(default={},
        help_text="""A JSON object to hold general settings for this Org""")

    def __unicode__(self):
        return "%s" % self.name

class Location(models.Model):
    org = models.ForeignKey(Org)
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)

    attrs = JSONField(default={},
        help_text="""A JSON object to hold general settings for this Org""")    

class Profile(models.Model):
    user = models.OneToOneField(User)
    orgs = models.ManyToManyField('Org', blank=True)
    attrs = JSONField(default={},
        help_text="A JSON object to hold general preferences for this user.")
    
    def __unicode__(self):
        return "%s" % self.user

    @property
    def org(self):
        """
        Return the first org
        """

        if self.orgs.all():
            return self.orgs.all()[0]
        else:
            return None

    @property
    def api_token(self):
        token = Token.objects.filter(user=self.user)
        if token:
            return token[0].key

    @property
    def org_names(self):
        return [org.name for org in self.orgs.all()]

    @property
    def org_dicts(self):
        return [{'name':org.name, 'id':org.id} for org in self.orgs.all()]



@receiver(post_save, sender=User)
def user_post_save(sender, instance=None, created=False, **kwargs):
    """
    Create a token and profile for the user
    """
    if created:
        Token.objects.create(user=instance)
        Profile.objects.create(user=instance)