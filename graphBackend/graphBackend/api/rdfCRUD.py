__author__ = 'mpetyx'

import rdflib
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import FOAF
from rdflib import RDF, BNode, Literal


class handler(object):
    database = 'SQLite'
    configString = "testdata.db"

    def __init__(self):
        g = rdflib.Graph(self.database)
        g.open(self.configString, create=False)
        self._graph = g

    def delete(self):
        query = prepareQuery(
            'delete { ?s ?p ?o } WHERE { ?person foaf:knows ?s .}',
            initNs={"foaf": FOAF})

        tim = rdflib.URIRef("http://www.w3.org/People/Berners-Lee/card#i")

        for row in self._graph.query(query, initBindings={'person': tim}):
            print row

        return query

    def get_object_list(self):
        query = self._graph.query("select * where {?s ?p ?o}")

        return query

    def obj_create(self):
        temp = BNode()
        self._graph.add((temp, RDF.type, FOAF.Person))
        self._graph.add((temp, FOAF.name, Literal("value", lang="en")))

    def obj_update(self, bundle, request=None, **kwargs):
        # return self.obj_create(bundle, request, **kwargs)

        self._graphg.update('''
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia: <http://dbpedia.org/resource/>
    INSERT
        { ?s a dbpedia:Human . }
    WHERE
        { ?s a foaf:Person . }
    ''')