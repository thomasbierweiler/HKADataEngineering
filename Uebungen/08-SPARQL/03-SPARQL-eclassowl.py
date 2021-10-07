# http://www.heppnetz.de/projects/eclassowl/
from rdflib import Graph
g = Graph().parse("http://www.heppnetz.de/files/eclassdemo.rdf")

#  Find all product models ("datasheets") of pencils that have a pointed tip.
q = """
    PREFIX eco: <http://www.ebusiness-unibw.org/ontologies/eclass/5.1.4/#>
    PREFIX gr: <http://purl.org/goodrelations/v1#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?model WHERE
    {
        ?model a eco:C_AKF303003-gen.
        ?model a gr:ProductOrServiceModel.
        ?model eco:P_BAG073001 eco:V_BAC386001.
        # Design of tip state [BAG073001] = "pointed" [BAC386001]
    }
"""
# Apply the query to the graph and iterate through results
for r in g.query(q):
    print('Datasheet for pencil with a pointed tip is available at {}.'.format(r['model']))

# Find all offers that include at least one pencil with a pointed tip.
q = """
    PREFIX eco: <http://www.ebusiness-unibw.org/ontologies/eclass/5.1.4/#>
    PREFIX gr: <http://purl.org/goodrelations/v1#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?company ?offer ?currency ?amount
    WHERE
    {
        ?company gr:offers ?offer.
        ?offer a gr:Offering.
        ?offer gr:hasBusinessFunction gr:Sell.
        ?offer gr:hasPriceSpecification ?price.
        ?price a gr:UnitPriceSpecification.
        ?price gr:hasCurrency ?currency.
        ?price gr:hasCurrencyValue ?amount.
        ?offer gr:includesObject ?o.
        ?o a gr:TypeAndQuantityNode.
        ?o gr:amountOfThisGood ?qtty.
        ?o gr:hasUnitOfMeasurement "C62"^^xsd:string.
        ?o gr:typeOfGood ?type.
        ?type a eco:C_AKF303003-gen.
        {
            {?type a gr:ActualProductOrServiceInstance.}
        UNION
            {?type a gr:ProductOrServicesSomeInstancesPlaceholder.}
        }
        ?type eco:P_BAG073001 eco:V_BAC386001.
        FILTER (?qtty >=1)
    }
"""
# Apply the query to the graph and iterate through results
for r in g.query(q):
    print('Company {} offers {}, currency {}, amount {}.'.format(r['company'],r['offer'],r['currency'],r['amount']))
    
