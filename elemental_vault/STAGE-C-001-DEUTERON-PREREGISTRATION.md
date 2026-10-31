# Stage C-001 preregistration — proton–neutron binding (deuteron)

**Project:** Elemental Vault / LVT  
**Status:** PREREGISTERED PLAN — no nuclear generator executed; no results claimed  
**Research lead:** Timothy; implementation proposed for Claude; independent review by GPT  
**Parent specification:** [RFC-001](./RFC-001-HYDROGEN-ORIGIN-SIMULATION.md)  
**Database:** Neon project `fragrant-hat-06859373`, database `elemental_vault`

## Discussion and problem
Timothy wants physical relationships and indexed ratios to drive an actual physics calculation, not merely a registry. The hydrogen ratio grid contains masses, length scales, and environmental quantities, but has not produced a nucleus. The first controlled nuclear target is the proton–neutron bound state (deuteron), a necessary intermediate toward hydrogen-to-helium synthesis, **not** a demonstration of helium production.

## Hypothesis
A specified two-body proton–neutron potential, calibrated **only** to an explicitly disclosed set of low-energy two-nucleon scattering observations, will produce a bound-state solution whose binding energy can be compared to a separately held-out deuteron binding-energy measurement. The result is a **scattering-calibrated reproduction**, not a discovery independent of all deuteron information.

## Model and equations to pin before running
1. Use proton and neutron masses from the approved ratio-grid inputs; reduced mass `μ = m_p m_n/(m_p + m_n)`; `ħc` and unit conventions explicitly sourced.
2. Start with a radial, finite spherical square-well potential `V(r)=-V0` for `r<R`, zero otherwise, in the spin-triplet S-wave channel. Solve the radial Schrödinger equation for negative-energy bound states by matching the interior/exterior logarithmic derivatives, with documented numerical tolerances. If spin coupling, tensor mixing, Coulomb, relativistic effects, or D-state admixture are omitted, mark them omitted.
3. Fix `R` and `V0` using **triplet-channel** scattering length and effective range, with precise values, sources, uncertainties, conventions, and fitting algorithm pinned in an input manifest before any bound-state calculation. Do **not** use the singlet-channel scattering length by mistake.
4. Define a physically meaningful domain and root-selection rule in advance; report multiple/no solutions rather than selecting the one closest to the target.
5. Hold out deuteron binding energy, mass and radius from all generator-visible inputs and execution paths. Disclose that scattering observables are themselves influenced by the near-threshold deuteron pole, making this a partially dependent blind test.

## Security gate — must pass before generator execution
- Create a dedicated login role `elemental_vault_generator` with **no** SUPERUSER, CREATEDB, CREATEROLE, BYPASSRLS or ownership privileges.
- Explicitly revoke default schema/table privileges where necessary. Grant CONNECT on the database, USAGE on `ratio_grid`, SELECT only on approved input/quantity tables, and only the minimal INSERT/SELECT needed on a separate generator-output table or approved prediction table. Avoid broad write access and avoid ownership of any reference objects.
- Grant **no** USAGE or SELECT on `reference_heldout` and no membership in a role that can read it. Check PUBLIC and inherited grants, default privileges, functions, views, SECURITY DEFINER paths, and role inheritance as relevant.
- Verify **as the generator role**: allowed input read succeeds, authorized prediction write succeeds using a rollback-only probe or equivalent, and reference schema/table reads fail with permission errors. Record the role used and the actual outcomes. A separate schema by itself is not proof of isolation.
- Keep role credentials private and server-side. Do not publish passwords or connection strings. Do not let the generator execute with owner credentials.
- Record an immutable fingerprint of the permitted inputs and implementation before opening held-out measurements.

## Planned tests and expected results
**Positive:** solver returns finite bound-state energy from scattering-calibrated potential, numerical convergence under refinement, and normalized radial state with physically consistent units. Conservation/normalization residuals and uncertainties are logged.

**Negative/tamper:** deny direct generator-role SELECT on held-out deuteron reference; deny unauthorized writes; deliberately alter an input or source fingerprint and ensure validation fails. Confirm the generator does not import reference data via files, source code, SQL views, or logs.

**Sensitivity:** perturb scattering length/effective range within stated uncertainties; vary square-well approximation or radius selection only according to preregistered rules; report binding-energy sensitivity and non-uniqueness. Optional independent check: predict a low-energy scattering observable **not used in calibration**, if an appropriate genuinely independent measurement is available.

**Comparison:** only after prediction is frozen, a separate evaluator reads `reference_heldout` and reports predicted binding energy versus measured ~2.2246 MeV, absolute/relative errors and uncertainty; do not optimize parameters against that target.

## Falsification and limitations
The hypothesis is challenged by no physically valid bound state, failure of the scattering fit, non-unique parameter solutions, unstable numerical results, large held-out disagreement, or input leakage. A close fit is **not** evidence that the model independently discovered deuterium, because the scattering calibration already constrains the deuteron pole. A square well is an intentionally simplified nuclear force and does not establish realistic nucleosynthesis rates, weak-interaction physics, or helium formation.

## Execution and reporting protocol
No generator or repository test runs are authorized by this document alone. Before each test run, publish a pre-test entry in GitHub Issue/Discussion recording Timothy's relevant direction, exact code/input pins, test method, expectations, and falsifiers. Afterward post in the same thread with observed outputs, interpretation separately, deviations, failures, artifacts, and next steps. Preserve original predictions and timestamps. No private material in public posts.

## Next step
Establish and verify the restricted Neon role; then Claude can propose/pin the scattering dataset and square-well implementation for Timothy's review. This document is a protocol, not a claim of completed execution.
