# https://rdflib.dev/sparqlwrapper/
from SPARQLWrapper import SPARQLWrapper, JSON

# set endpoint
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# Select Query
# Select translations for the Spanish Principality of Asturias
sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

print('##################################')
print('Labels (translations) for the Spanish Principality of Asturias')
print('Language\tTranslation')
for result in results["results"]["bindings"]:
    print('{}\t\t{}'.format(result["label"]["xml:lang"],result["label"]["value"]))
print('##################################')

print('Select names of persons who are of type FOAF:')
sparql.setQuery("""
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX : <http://dbpedia.org/resource/>
    PREFIX dbpedia2: <http://dbpedia.org/property/>
    PREFIX dbpedia: <http://dbpedia.org/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?name
    WHERE {
        ?p rdf:type foaf:Person .

        ?p foaf:name ?name .
    }
    LIMIT 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["name"]["value"])