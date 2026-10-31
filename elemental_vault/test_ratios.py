import unittest
from elemental_vault.ratios import Quantity,RatioRegistry,hydrogen_registry
class RatioTests(unittest.TestCase):
    def test_mass_ratio(self):self.assertAlmostEqual(hydrogen_registry().ratio('mass','proton_mass_kg','electron_mass_kg').value,1836.15,delta=0.02)
    def test_charge_ratio(self):self.assertEqual(hydrogen_registry().ratio('charge','proton_charge_abs_c','electron_charge_abs_c').value,1)
    def test_scale_ratio(self):self.assertAlmostEqual(hydrogen_registry().ratio('scale','bohr_radius_m','proton_charge_radius_m').value,63000,delta=100)
    def test_mismatch_rejected(self):
        with self.assertRaises(ValueError):hydrogen_registry().ratio('bad','proton_mass_kg','bohr_radius_m')
    def test_external_measurement_rejected(self):
        with self.assertRaises(PermissionError):hydrogen_registry().add(Quantity('helium_energy',28.3,'energy','external_measurement'))
    def test_external_measurement_allowed_in_validation(self):
        r=RatioRegistry(strict=False);r.add(Quantity('helium_energy',28.3,'energy','external_measurement'));self.assertIn('helium_energy',r.quantities)
    def test_translation_invariance(self):
        r=hydrogen_registry();a=(0,0,0);b=(5.29177210903e-11,0,0)
        first=r.distance_ratio('d1',a,b,'bohr_radius_m').value
        shift=(1e-8,-2e-8,3e-8)
        second=r.distance_ratio('d2',tuple(x+y for x,y in zip(a,shift)),tuple(x+y for x,y in zip(b,shift)),'bohr_radius_m').value
        self.assertAlmostEqual(first,second,places=10)
    def test_zero_denominator(self):
        r=hydrogen_registry();r.add(Quantity('zero',0,'mass','derived'))
        with self.assertRaises(ZeroDivisionError):r.ratio('bad','proton_mass_kg','zero')
