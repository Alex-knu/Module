from rdflib import Graph, URIRef

g = Graph()
country = {}

g.parse("countries_info.ttl")

for s, p, o in g:
    country_neighbour_value = g.value(subject=s, predicate=URIRef("http://example.com/demo/country_neighbour_value"))

    if country.get(str(country_neighbour_value)) is not None:
        country[str(country_neighbour_value)] += 1
        continue
    
    country[str(country_neighbour_value)] = 1


country.pop('None', None)
max_key = max(country, key=lambda k: country[k])
max_value = country[max_key]

print("Country:", max_key)
print("Value:", max_value)