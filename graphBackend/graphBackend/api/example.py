__author__ = 'mpetyx'

from rdflib import ConjunctiveGraph

# default_graph_uri = URIRef("http://rdflib.net/data")

graph = ConjunctiveGraph('SQLite')#, identifier=default_graph_uri)
configString = "testdata.db"

graph.open(configString, create=False)
# linda = BNode()
# graph.add( (linda,FOAF.name, Literal("linda2",lang="en")) )
# graph.add( (linda,FOAF.nickname, Literal("koukla2",lang="en")) )
# graph.commit()
# graph.close()

for row in graph.query("select * where {?s ?p ?o}"):
    print row



