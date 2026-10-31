"""Read-only Elemental Vault API; no secrets or Neon access exposed."""
from flask import Flask, jsonify, request
from elemental_vault.experiment import report
from elemental_vault.physics import binding_energy_mev
app = Flask(__name__)
@app.get('/health')
def health(): return jsonify(status='ok',engine='elemental-vault-v1')
@app.get('/experiment')
def experiment(): return jsonify(report())
@app.get('/candidate')
def candidate():
    try:
        z=int(request.args['z']); n=int(request.args['n'])
        if z>118 or n>250: raise ValueError('outside configured bounds')
        b=binding_energy_mev(z,n)
        return jsonify(Z=z,N=n,A=z+n,binding_mev=round(b,4),status='unvalidated_candidate')
    except (KeyError,ValueError,OverflowError) as exc:
        return jsonify(error=str(exc)),400
