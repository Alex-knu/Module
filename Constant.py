request_3 = '''
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbp: <http://dbpedia.org/property/>
    SELECT DISTINCT ?disease ?method
    WHERE {
      ?disease a dbo:Disease ;
               dbp:field dbr:Gastroenterology .
      OPTIONAL { ?disease dbp:diagnosticMethod ?method }
    }
''' 