# source: https://www.dbpedia.org/resources/sparql/
# Select all soccer players who were born in a country with more than 10 million inhabitants,
# who played as goalkeeper for a club that has a stadium with more than 30,000 seats,
# and whose club country is/was different from their birth country.
# Print only the names of the soccer players.

from SPARQLWrapper import SPARQLWrapper, JSON

# set endpoint
sparql=SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
   SELECT distinct ?name # ?soccerplayer ?countryOfBirth ?team ?countryOfTeam ?stadiumcapacity
   WHERE { 
      # ensure that the soccer player is of type person
      ?soccerplayer rdf:type foaf:Person .
      # select the name of the soccer player
      ?soccerplayer foaf:name ?name .
      # get all entities of type soccer player
      ?soccerplayer a dbo:SoccerPlayer ; # "a" is a short cut for rdf:type
         # limit to soccer players who are goal keepers
         dbo:position|dbp:position <http://dbpedia.org/resource/Goalkeeper_(association_football)> ;
         # get the country of birth
         dbo:birthPlace/dbo:country* ?countryOfBirth ;
         # get the team of the soccer player
         dbo:team ?team .
      # for the team, get the capacity of the stadium and the country of the team
      ?team dbo:capacity ?stadiumcapacity ; dbo:ground ?countryOfTeam .
      # for the country of birth, get the population
      ?countryOfBirth rdf:type dbo:Country ; dbo:populationTotal ?population .
      # restrict the country of the team to type country
      ?countryOfTeam rdf:type dbo:Country .
      # remove empty names
      FILTER(str(?name) != "")
      # whose club country is/was different from their birth country
      FILTER (?countryOfTeam != ?countryOfBirth)
      # for a club that has a stadium with more than 30,000 seats
      FILTER (?stadiumcapacity > 30000)
      # who were born in a country with more than 10 million inhabitants
      FILTER (?population > 10000000)
   } order by ?name
""")

sparql.setReturnFormat(JSON)
results=sparql.query().convert()
for result in results["results"]["bindings"]:
    """
    print(result["soccerplayer"]["value"])
    print(result["countryOfBirth"]["value"])
    print(result["team"]["value"])
    print(result["countryOfTeam"]["value"])
    print(result["stadiumcapacity"]["value"])
    """
    print('name of goal keeper: {}'.format(result["name"]["value"]))
