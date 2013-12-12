__author__ = 'mpetyx'

from tastypie.resources import Resource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie import fields

from rdfConnector import rdfClient
from RdfObject import RdfObject


class PersonResource(Resource):
    # Just like a Django ``Form`` or ``Model``, we're defining all the
    # fields we're going to handle with the API here.
    uuid = fields.CharField(attribute='uuid')
    user_uuid = fields.CharField(attribute='user_uuid')
    age = fields.CharField(attribute='age')
    created = fields.IntegerField(attribute='created')

    class Meta:
        resource_name = 'person'
        object_class = RdfObject
        authorization = Authorization()

    # Specific to this resource, just to get the needed Riak bits.
    def _client(self):
        return rdfClient()

    def _bucket(self):
        client = self._client()
        # Note that we're hard-coding the bucket to use. Fine for
        # example purposes, but you'll want to abstract this.
        return client.bucket('messages')

    # The following methods will need overriding regardless of your
    # data source.
    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.uuid
        else:
            kwargs['pk'] = bundle_or_obj.uuid

        return kwargs

    def get_object_list(self, request):
        # query = self._client().add('messages')
        # query.map("function(v) { var data = JSON.parse(v.values[0].data); return [[v.key, data]]; }")
        # results = []
        #
        # for result in query.run():
        #     new_obj = RdfObject(initial=result[1])
        #     new_obj.uuid = result[0]
        #     results.append(new_obj)
        results = []

        return results

    def obj_get_list(self, request=None, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(request)

    def obj_get(self, request=None, **kwargs):
        bucket = self._bucket()
        message = bucket.get(kwargs['pk'])
        return RdfObject(initial=message.get_data())

    def obj_create(self, bundle, request=None, **kwargs):
        bundle.obj = RdfObject(initial=kwargs)
        bundle = self.full_hydrate(bundle)
        bucket = self._bucket()
        new_message = bucket.new(bundle.obj.uuid, data=bundle.obj.to_dict())
        new_message.store()
        return bundle

    def obj_update(self, bundle, request=None, **kwargs):
        return self.obj_create(bundle, request, **kwargs)

    def obj_delete_list(self, request=None, **kwargs):
        bucket = self._bucket()

        for key in bucket.get_keys():
            obj = bucket.get(key)
            obj.delete()

    def obj_delete(self, request=None, **kwargs):
        bucket = self._bucket()
        obj = bucket.get(kwargs['pk'])
        obj.delete()

    def rollback(self, bundles):
        pass