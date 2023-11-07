from Constant import request_3
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, JSON


sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery(request_3)
sparql.setReturnFormat(JSON)

results = sparql.query().convert()

g = Graph()

#Create triples
for result in results["results"]["bindings"]:
    disease = result["disease"]["value"]
    method = result.get("method", {})
    g.add((URIRef(disease), URIRef("http://dbpedia.org/property/diagnosticMethod"), URIRef(method)))

for disease, p, method in g.triples((None, URIRef("http://dbpedia.org/property/diagnosticMethod"), None)):
    print("Посилання:", disease)
    print("Метод діагностики:", method)
    print("\n")