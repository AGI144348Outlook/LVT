import unittest
from elemental_vault.spatial import hydrogen_seed, coulomb_force_on_first, translate
class SpatialTests(unittest.TestCase):
    def test_hydrogen_particle_content(self):
        s=hydrogen_seed()
        self.assertEqual(len(s.particles),2)
        self.assertEqual(sum(p.charge_e for p in s.particles),0)
    def test_coulomb_equal_opposite(self):
        a,b=hydrogen_seed().particles
        f=coulomb_force_on_first(a,b); g=coulomb_force_on_first(b,a)
        for x,y in zip(f,g): self.assertAlmostEqual(x,-y,delta=max(abs(x),abs(y))*1e-12)
        self.assertGreater(f[0],0)
    def test_translation_preserves_force(self):
        s=hydrogen_seed(); moved=translate(s,(1e-9,0,0))
        f=coulomb_force_on_first(*s.particles); g=coulomb_force_on_first(*moved.particles)
        for x,y in zip(f,g): self.assertAlmostEqual(x,y,delta=max(abs(x),abs(y))*1e-10)
    def test_reference_isolation(self):
        import inspect, elemental_vault.spatial as s
        self.assertNotIn('from elemental_vault.reference',inspect.getsource(s))
