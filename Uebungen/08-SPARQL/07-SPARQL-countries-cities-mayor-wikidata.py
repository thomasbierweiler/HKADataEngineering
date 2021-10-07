# source: https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples/advanced#List_of_countries_ordered_by_the_number_of_their_cities_with_female_mayor
# List of countries ordered by the number of their cities with female mayor

from SPARQLWrapper import SPARQLWrapper, JSON

# set endpoint
sparql=SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
sparql.setQuery("""
  SELECT ?country ?countryLabel ?officialName (count(*) AS ?count)
WHERE
{
	?city wdt:P31/wdt:P279* wd:Q515 . # find instances of subclasses of city
	?city p:P6 ?statement .           # with a P6 (head of goverment) statement
	?statement ps:P6 ?mayor .         # ... that has the value ?mayor
	?mayor wdt:P21 wd:Q6581072 .      # ... where the ?mayor has P21 (sex or gender) female
	FILTER NOT EXISTS { ?statement pq:P582 ?x }  # ... but the statement has no P582 (end date) qualifier
	?city wdt:P17 ?country .          # Also find the country of the city
	# If available, get the "de" label of the country, use "en" as fallback:
	SERVICE wikibase:label {
		bd:serviceParam wikibase:language "de,en" .
	}
   ?country wdt:P1448 ?officialName .          # get the official names of the country
}
GROUP BY ?country ?countryLabel ?officialName
ORDER BY DESC(?count)
LIMIT 100
""")

sparql.setReturnFormat(JSON)
results=sparql.query().convert()
for result in results["results"]["bindings"]:
    print('{}\t{}\t{}\t{}'.format(result["country"]["value"],result["countryLabel"]["value"],result["officialName"]["value"],result["count"]["value"]))
