"""Read-only numerical comparison: generator never imports reference."""
import json
from elemental_vault.physics import binding_energy_mev, predicted_nuclei, COEFF
from elemental_vault.reference import REFERENCE
def report():
    rows=[]
    for name,z,n,observed in REFERENCE:
        predicted=binding_energy_mev(z,n)
        rows.append(dict(isotope=name,Z=z,N=n,predicted_mev=round(predicted,4),reference_mev=observed,
                         signed_error_mev=round(predicted-observed,4),absolute_error_mev=round(abs(predicted-observed),4)))
    return {'model':'SEMF (empirical coefficients, NOT hydrogen-only discovery)', 'coefficients':COEFF,
            'comparison':rows,'mae_mev':round(sum(r['absolute_error_mev'] for r in rows)/len(rows),4),
            'candidate_count_z2_to26':sum(1 for _ in predicted_nuclei()),
            'limitations':'No reaction kinetics, synthesis rates, electron structure, isotope stability or quantum nuclear solver.'}
if __name__=='__main__': print(json.dumps(report(),indent=2))
