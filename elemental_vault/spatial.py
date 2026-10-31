"""Hydrogen-first spatial representation; classical force demonstration only.

Not a quantum orbital solver or a fusion simulation. No element reference data.
"""
from dataclasses import dataclass
from math import sqrt
from typing import Tuple

COULOMB_K = 8.9875517923e9
ELEMENTARY_CHARGE_C = 1.602176634e-19
BOHR_RADIUS_M = 5.29177210903e-11  # established universal atomic scale, not a fitted He value
Vec3 = Tuple[float, float, float]

@dataclass(frozen=True)
class Particle:
    kind: str
    charge_e: int
    position_m: Vec3

@dataclass(frozen=True)
class SpatialState:
    particles: Tuple[Particle, ...]
    label: str
    interpretation: str

def hydrogen_seed() -> SpatialState:
    return SpatialState((
        Particle("proton", 1, (0.0, 0.0, 0.0)),
        Particle("electron", -1, (BOHR_RADIUS_M, 0.0, 0.0)),
    ), "hydrogen-1", "Illustrative point coordinates only; not an electron trajectory or orbital probability density")

def coulomb_force_on_first(a: Particle, b: Particle) -> Vec3:
    """Force vector acting on a due to b, using classical Coulomb's law."""
    d = tuple(a.position_m[i] - b.position_m[i] for i in range(3))
    r2 = sum(v*v for v in d)
    if r2 <= 0: raise ValueError("Point charges cannot overlap")
    f = COULOMB_K * a.charge_e * b.charge_e * ELEMENTARY_CHARGE_C**2 / (r2 * sqrt(r2))
    return tuple(f*v for v in d)

def translate(state: SpatialState, shift_m: Vec3) -> SpatialState:
    return SpatialState(tuple(Particle(p.kind, p.charge_e, tuple(p.position_m[i]+shift_m[i] for i in range(3))) for p in state.particles),state.label,state.interpretation)
