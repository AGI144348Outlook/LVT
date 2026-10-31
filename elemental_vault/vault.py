"""Elemental Vault v0: conservation-first nuclear reaction ledger.

Not a quantum nuclear solver. No periodic-table answer key is imported.
"""
from dataclasses import dataclass
from collections import Counter
from typing import Mapping

@dataclass(frozen=True)
class Species:
    name: str
    charge: int
    baryons: int
    lepton_e: int = 0

PROTON = Species("proton", 1, 1)
NEUTRON = Species("neutron", 0, 1)
ELECTRON = Species("electron", -1, 0, 1)
POSITRON = Species("positron", 1, 0, -1)
NU_E = Species("electron_neutrino", 0, 0, 1)
GAMMA = Species("photon", 0, 0)
DEUTERON = Species("deuteron", 1, 2)
HELIUM3 = Species("helium_3_nucleus", 2, 3)
HELIUM4 = Species("helium_4_nucleus", 2, 4)
HYDROGEN1 = {"protons": 1, "neutrons": 0, "electrons": 1, "atomic_number": 1}

def totals(items: Mapping[Species, int]) -> tuple[int, int, int]:
    if any(not isinstance(n, int) or n < 0 for n in items.values()):
        raise ValueError("Stoichiometric coefficients must be nonnegative integers")
    return tuple(sum(getattr(s, key) * n for s, n in items.items())
                 for key in ("charge", "baryons", "lepton_e"))

def balanced(reactants: Mapping[Species, int], products: Mapping[Species, int]) -> bool:
    return totals(reactants) == totals(products)

# Net pp-I chain. Neutrinos and positrons are required for lepton/charge accounting.
PP_I_NET_REACTANTS = {PROTON: 4}
PP_I_NET_PRODUCTS = {HELIUM4: 1, POSITRON: 2, NU_E: 2, GAMMA: 2}

def candidate_from_nucleons(protons: int, neutrons: int) -> dict:
    """Construct an UNVALIDATED nucleus candidate; does not predict stability."""
    if not isinstance(protons, int) or not isinstance(neutrons, int) or protons < 1 or neutrons < 0:
        raise ValueError("Nucleon counts must be integers; protons >= 1; neutrons >= 0")
    return {"Z": protons, "N": neutrons, "A": protons + neutrons,
            "charge_e": protons, "status": "unvalidated_candidate"}

def first_candidate() -> dict:
    if not balanced(PP_I_NET_REACTANTS, PP_I_NET_PRODUCTS):
        raise RuntimeError("Net pp-I ledger failed conservation")
    return candidate_from_nucleons(2, 2)
