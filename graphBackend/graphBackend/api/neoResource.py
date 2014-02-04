__author__ = 'mpetyx'


from tastypie.resources import ModelResource
from Neo4JModel import Entry

class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'