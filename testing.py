# Testing
# Tests are implemented in the tests/ directory to ensure all components work seamlessly. 
# For example, the test for the ontology manager:

import unittest
from ontologika.data.ontology_manager import OntologyManager

class TestOntologyManager(unittest.TestCase):
    def setUp(self):
        self.manager = OntologyManager("tests/test_ontology.owl")

    def test_query_relationships(self):
        result = self.manager.query_relationships("User", "hasProfile")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
