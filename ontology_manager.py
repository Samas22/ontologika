# 2. Ontology Manager (ontology_manager.py)
# Handles semantic reasoning using OWL and RDF.


from owlready2 import get_ontology, Thing, default_world

class OntologyManager:
    def __init__(self, ontology_path):
        self.ontology = get_ontology(ontology_path).load()

    def query_relationships(self, subject, predicate=None):
        """
        Query relationships within the ontology.
        """
        if predicate:
            return [(s, p, o) for s, p, o in self.ontology.get_triples() if s == subject and p == predicate]
        return [(s, p, o) for s, p, o in self.ontology.get_triples() if s == subject]

    def infer(self):
        """
        Run reasoning to infer new facts.
        """
        default_world.infer()

# Example usage
ontology_manager = OntologyManager("path/to/ontology.owl")
relationships = ontology_manager.query_relationships("User", "hasProfile")
