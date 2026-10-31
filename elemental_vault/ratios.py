from dataclasses import dataclass
from math import dist,isfinite
ALLOWED=frozenset(('hydrogen_seed','universal_constant','derived'))
@dataclass(frozen=True)
class Quantity:
    key:str
    value:float
    dimension:str
    provenance:str
    def __post_init__(self):
        if self.provenance not in ALLOWED|{'external_measurement'}:raise ValueError('unknown provenance')
        if not isfinite(self.value):raise ValueError('nonfinite quantity')
@dataclass(frozen=True)
class Ratio:
    key:str
    numerator:str
    denominator:str
    value:float
    dimension:str
class RatioRegistry:
    def __init__(self,strict=True):self.strict=strict;self.quantities={};self.ratios={}
    def add(self,q):
        if self.strict and q.provenance not in ALLOWED:raise PermissionError('external measurement forbidden')
        if q.key in self.quantities:raise ValueError('duplicate key')
        self.quantities[q.key]=q
    def ratio(self,key,a,b):
        x,y=self.quantities[a],self.quantities[b]
        if x.dimension!=y.dimension:raise ValueError('dimension mismatch')
        if y.value==0:raise ZeroDivisionError('zero denominator')
        r=Ratio(key,a,b,x.value/y.value,x.dimension);self.ratios[key]=r;return r
    def distance_ratio(self,key,a,b,reference_key):
        ref=self.quantities[reference_key]
        if ref.dimension!='length' or ref.value<=0:raise ValueError('invalid length reference')
        r=Ratio(key,'distance:pair',reference_key,dist(a,b)/ref.value,'length')
        self.ratios[key]=r;return r
def hydrogen_registry():
    r=RatioRegistry()
    for q in (
        Quantity('proton_mass_kg',1.67262192369e-27,'mass','hydrogen_seed'),
        Quantity('electron_mass_kg',9.1093837139e-31,'mass','hydrogen_seed'),
        Quantity('proton_charge_abs_c',1.602176634e-19,'charge','universal_constant'),
        Quantity('electron_charge_abs_c',1.602176634e-19,'charge','universal_constant'),
        Quantity('bohr_radius_m',5.29177210903e-11,'length','derived'),
        Quantity('proton_charge_radius_m',0.84e-15,'length','hydrogen_seed'),
    ):r.add(q)
    return r
