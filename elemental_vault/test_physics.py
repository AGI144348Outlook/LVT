import unittest
from math import isfinite
from elemental_vault.physics import binding_energy_mev, predicted_nuclei
from elemental_vault.experiment import report
class PhysicsTests(unittest.TestCase):
    def test_finite_helium(self): self.assertTrue(isfinite(binding_energy_mev(2,2)))
    def test_invalid_hydrogen(self):
        with self.assertRaises(ValueError): binding_energy_mev(1,0)
    def test_candidate_enumeration(self):
        xs=list(predicted_nuclei(2,3))
        self.assertTrue(xs)
        self.assertTrue(all(x['status']=='unvalidated_candidate' for x in xs))
    def test_validation_has_errors(self):
        r=report()
        self.assertEqual(len(r['comparison']),5)
        self.assertGreater(r['mae_mev'],0)
    def test_generator_has_no_reference_import(self):
        import inspect, elemental_vault.physics as p
        self.assertNotIn('reference',inspect.getsource(p))
