__author__ = 'mpetyx'


# from neo4django.auth.models import User
# from django.contrib.auth.models import User
from neo4django.graph_auth.models import User
from neo4django.db import models
from django.template.defaultfilters import slugify

"""
    or this is also working
    https://gist.github.com/mhluongo/5789513

    taken from http://stackoverflow.com/questions/16920180/create-rest-api-with-neo4j-and-django
"""

class Entry(models.NodeModel):
    user = models.Relationship(User, related_name='entries',
                               rel_type='authored_by', single=True)
    pub_date = models.DateTimeProperty(auto_now=True)
    title = models.StringProperty(indexed=True)
    slug = models.StringProperty()
    body = models.StringProperty()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)