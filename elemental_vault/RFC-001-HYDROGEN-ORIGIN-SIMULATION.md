# RFC-001 — Hydrogen-Origin Physical Simulation
**Project:** Elemental Vault (LVT)  
**Status:** DRAFT — Timothy review required; not approved for implementation  
**Scope:** Hydrogen-origin physical simulation and blind comparison to measured elemental properties  
**Version:** 0.1

## 1. Research question
Given a specified initial inventory of hydrogen and explicitly allowed physical laws/constants, can an executable physical model generate nuclear reaction products, including helium and progressively heavier nuclei, without reading the measured properties, abundances, structures, or names of target elements? How accurately do the generated products compare with independently held-out measurements?

**No predetermined helium output is permitted.** A conventional proton-proton reaction pathway can be used as a benchmark, but cannot be described as independently discovered by the model.

## 2. Input boundary (explicitly declared)
- **Seed material:** hydrogen-1 atoms and/or ionized hydrogen plasma, with user-selected count, initial positions/velocities or quantum state representation, temperature, density, pressure, and time horizon. Starting conditions must be stated; hydrogen alone is not enough to specify fusion.
- **Permitted physical knowledge:** dimensional constants and fundamental interaction models (electromagnetism, weak interactions, nuclear strong-force approximations, quantum mechanics, conservation laws, particle rest masses and coupling parameters) only when their provenance and calibration are declared.
- **Important distinction:** nuclear interaction parameters and neutron properties are not logically derivable from one hydrogen atom alone. Every empirical input beyond the hydrogen seed must be tagged. Run modes: **strict hydrogen-observation only** (likely underdetermined), **hydrogen + established universal physics** (main scientific mode), and **empirical benchmark** (not eligible for blind discovery claims).
- **Forbidden to generator:** reference tables of elemental/isotopic masses and binding energies beyond authorized hydrogen inputs; target-element identities, desired compositions, output templates, and target-specific fitted coefficients.
- **Reference evaluator:** isolated process/data boundary with access to measured nuclide properties only after a candidate prediction is finalized and recorded.

## 3. Quantities, indexed ratios and spatial representations
Each quantity has an ID, numeric value, unit/dimension, uncertainty where known, provenance, and permission class. Ratio records contain numerator/denominator IDs, operation, value, and time/frame where applicable.

Illustrative records: proton/electron mass ratio; proton/electron charge magnitude ratio; characteristic atomic length/proton charge radius; interparticle distance/reference length; force ratios; energy/rest-energy ratios; time-scale ratios. Ratios are dimensionless only for commensurable quantities. Zero denominators and unit mismatches are errors.

Spatial representation supports both (a) interparticle geometry and (b) internal particle structure **where physically meaningful**. The proton may have a modeled charge distribution; the electron is not assigned a fictitious measured hard-sphere radius. Quantum probability densities are distinguished from classical particle trajectories. Pairwise distance ratios require geometrically realizable configurations. Reference frames, orientation, translation, and uncertainty are specified.

## 4. Physics and dynamics
Define state, interactions, transition operators, timestep or event-driven solver, conserved quantities, energy exchange, and stopping criteria. A simple Coulomb point-particle model is a geometry demonstration, **not** a fusion or atomic quantum solver.

A viable nuclear model must address: Coulomb barrier, tunneling or quantum reaction amplitudes, strong and weak interactions, relevant particle production, reaction Q values, thermal distributions, and reaction rates. Products are generated from allowed transitions rather than enumerated from the periodic table. Reaction chains must track nucleons, charge, leptons, energy/momentum, and neutrino/photon emissions where applicable.

Numerical approximation and calibration provenance are mandatory. If an interaction is omitted, the experiment must report that the corresponding synthesis claim is unsupported.

## 5. Experimental progression
**Stage A — dimensional and spatial foundation:** hydrogen seed, indexed ratios, geometry consistency, unit checks, provenance isolation. No element-production claim.

**Stage B — hydrogen physics calibration:** reproduce hydrogen observables permitted by the selected mode, checking numerical stability and conservation. No helium discovery claim.

**Stage C — nuclear reaction simulation:** with specified plasma environment and permitted physics, attempt hydrogen-to-heavier-product transitions; record every attempted transition, rate/probability, and final product. A benchmark with the known pp-chain is explicitly labeled *guided benchmark*.

**Stage D — blind validation:** freeze generated candidate records; evaluator separately compares predicted Z, A, nuclear mass/binding energy, stability/decay and yields when the model supports them against a pinned, independently sourced nuclear-data release. Report error distributions and failures, not only matches.

**Stage E — extension:** attempt heavier nuclei only with modeled pathways and appropriate environmental conditions; stellar nucleosynthesis beyond helium is not expected from ordinary hydrogen conditions alone.

## 6. Success criteria
- **Engineering pass:** reproducible numerical execution, unit/dimension checks, conservation residuals within stated tolerances, immutable input manifest and output record, strict data isolation.
- **Physics pass:** observed product channels, energy balance and reaction rates agree with independent benchmarks within prespecified tolerances for the chosen physical model.
- **Blind-prediction pass:** predictions committed before evaluator accesses reference values, with target-property errors and provenance reported.
- **Discovery claim:** only if an unguided, properly blinded model produces a candidate and demonstrates physically valid formation dynamics; a lookup, fitted mass formula, hand-coded target product, or conservation-only check does not qualify.

## 7. Data and software requirements (specification, not authorization to build)
- Seed registry; physical quantity and indexed-ratio registry; spatial/quantum state records; interaction/reaction ledger; immutable experiment manifests; generated candidate registry; isolated validation dataset and evaluator.
- Python compute engine may run on Render; Neon may store manifests/results; Vercel may visualize results. These are **implementation options**, not scientific dependencies.
- All APIs must expose provenance, run configuration, units, uncertainty, solver version and whether results are observed, simulated, inferred, or benchmark-guided.
- Keep credentials server-side. No target-reference table available to the generator runtime.

## 8. Known limitations and falsifiers
- A single hydrogen atom does not determine the complete Standard Model or nuclear interaction parameters. A strictly hydrogen-observation-only run may be non-identifiable; report this as a result rather than silently inserting external information.
- Classical point particles cannot accurately reproduce quantum orbitals or fusion cross sections.
- Ratios encode relationships but do not independently supply dynamical laws.
- Unphysical energy balance, failed conservation, target-data leakage, sensitivity to hidden fitted parameters, or nonreproducible results invalidate relevant claims.
- Heavier-element formation requires environmental and reaction-pathway assumptions; not every nucleus is reachable under every condition.

## 9. Governance and next action
This RFC is **draft only**. Existing ratio/spatial/API code is provisional and does not establish scientific validity. Do not run new repository tests or extend implementation under this RFC until Timothy reviews it and the test protocol is preregistered in the repository Issue/Discussion. On approval, implement the smallest executable Stage A–C experiment, then run blinded validation and document observations separately from interpretations.

## 10. Questions for review
1. Is the main experiment **hydrogen + established physics**, with a separate strict hydrogen-observation-only run to expose what cannot be inferred?
2. What initial environment should be first: low-temperature atomic hydrogen, hot dense stellar-core-like hydrogen plasma, or both?
3. Which initial success target: a physically modeled helium-producing channel, or an unguided search for reaction products?
