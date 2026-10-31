"""Standard-library unit tests; no network or reference data."""
import unittest
from elemental_vault.vault import (
    HYDROGEN1, PROTON, HELIUM4, POSITRON, NU_E, GAMMA,
    PP_I_NET_REACTANTS, PP_I_NET_PRODUCTS, balanced,
    candidate_from_nucleons, first_candidate, totals,
)

class VaultTests(unittest.TestCase):
    def test_hydrogen_seed(self):
        self.assertEqual(HYDROGEN1["atomic_number"], 1)
        self.assertEqual(HYDROGEN1["protons"], 1)
        self.assertEqual(HYDROGEN1["electrons"], 1)

    def test_pp_chain_net_conservation(self):
        self.assertTrue(balanced(PP_I_NET_REACTANTS, PP_I_NET_PRODUCTS))
        self.assertEqual(totals(PP_I_NET_REACTANTS), (4, 4, 0))

    def test_tamper_rejects_missing_neutrinos(self):
        self.assertFalse(balanced(PP_I_NET_REACTANTS, {HELIUM4: 1, POSITRON: 2, GAMMA: 2}))

    def test_tamper_rejects_missing_positrons(self):
        self.assertFalse(balanced(PP_I_NET_REACTANTS, {HELIUM4: 1, NU_E: 2, GAMMA: 2}))

    def test_candidate_not_claimed_stable(self):
        self.assertEqual(first_candidate(), {"Z": 2, "N": 2, "A": 4, "charge_e": 2, "status": "unvalidated_candidate"})

    def test_reject_invalid_nucleons(self):
        for z, n in [(0, 1), (1, -1), (1.5, 1)]:
            with self.assertRaises(ValueError):
                candidate_from_nucleons(z, n)

if __name__ == "__main__":
    unittest.main()
