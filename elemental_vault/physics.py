"""Empirically calibrated liquid-drop model. NOT first-principles hydrogen discovery.
Coefficients in MeV, illustrative common SEMF set (not fitted to validation set).
"""
from math import isfinite
COEFF = dict(volume=15.8, surface=18.3, coulomb=0.714, asymmetry=23.2, pairing=12.0)
def binding_energy_mev(z: int, n: int) -> float:
    """SEMF for A>=2; no meaningful prediction for hydrogen-1."""
    if not isinstance(z, int) or not isinstance(n, int) or z < 1 or n < 0 or z+n < 2:
        raise ValueError('Requires integer Z>=1, N>=0, A>=2')
    a=z+n
    p=0.0 if a%2 else (COEFF['pairing']/a**0.5 if z%2==0 and n%2==0 else -COEFF['pairing']/a**0.5)
    return (COEFF['volume']*a-COEFF['surface']*a**(2/3)
            -COEFF['coulomb']*z*(z-1)/a**(1/3)
            -COEFF['asymmetry']*(a-2*z)**2/a+p)
def predicted_nuclei(z_min=2,z_max=26):
    """Enumerate mathematical candidates; do not claim any are produced or stable."""
    if not 1<=z_min<=z_max<=118: raise ValueError('invalid bounds')
    for z in range(z_min,z_max+1):
        for n in range(max(0,z-4),min(3*z+4,180)+1):
            b=binding_energy_mev(z,n)
            if isfinite(b) and b>0:
                yield {'Z':z,'N':n,'A':z+n,'binding_mev':round(b,4),'status':'unvalidated_candidate'}
