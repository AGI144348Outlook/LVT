# List-only repository directory mirror

Repository: `AGI144348Outlook/LVT`. Captured 2026-11-15. This is an initial list-only snapshot, not completed content auditing. Excluded root: `Contract000_Audit/` only. Branch IDs below are local list keys; ranges in the path table include every integer in the range. These are exact branch memberships, not samples. Source content is not embedded.

## Branch names and pinned commits

| ID | Branch name | Commit |
|---|---|---|
| 0 | `claude/github-claude-code-connection-98qkbx` | `bcd5b436008b912806c3b79b5bbfd46a8b05ec39` |
| 1 | `experiment/elemental-vault-v0` | `f3849394d0466e88696b970d655dee7920203832` |
| 2 | `main` | `122aeae062604c2128c9d3fa1a5beb3d64d0ca0a` |

## Every folder and filing by name

| Kind | Repository-relative name | Branch IDs |
|---|---|---|
| file | `contracts/.gitignore` | 0 |
| file | `contracts/EVE_Environment_Wrapper.sol` | 0-2 |
| file | `contracts/file_provenanve_protocol.md` | 0-2 |
| file | `contracts/LVT_1155_Nested_Standard.sol` | 0-2 |
| file | `contracts/README.md` | 0 |
| file | `demo/index.html` | 0 |
| file | `docs/link-to-fractal-grid-code.md` | 0 |
| file | `docs/lvt-token-ai-visualization-instructions.md` | 0 |
| file | `docs/manifold-engine-mvp-specs.md` | 0 |
| file | `docs/tech-spec.md` | 0 |
| file | `elemental_vault/__init__.py` | 1 |
| file | `elemental_vault/api.py` | 1 |
| file | `elemental_vault/experiment.py` | 1 |
| file | `elemental_vault/physics.py` | 1 |
| file | `elemental_vault/ratios.py` | 1 |
| file | `elemental_vault/README.md` | 1 |
| file | `elemental_vault/reference.py` | 1 |
| file | `elemental_vault/RFC-001-HYDROGEN-ORIGIN-SIMULATION.md` | 1 |
| file | `elemental_vault/schema.sql` | 1 |
| file | `elemental_vault/spatial.py` | 1 |
| file | `elemental_vault/STAGE-C-001-DEUTERON-PREREGISTRATION.md` | 1 |
| file | `elemental_vault/test_physics.py` | 1 |
| file | `elemental_vault/test_ratios.py` | 1 |
| file | `elemental_vault/test_spatial.py` | 1 |
| file | `elemental_vault/test_vault.py` | 1 |
| file | `elemental_vault/vault.py` | 1 |
| file | `elemental_vault/web/index.html` | 1 |
| file | `engine/.gitignore` | 0 |
| file | `engine/exponential_instancing_v1.math` | 0-2 |
| file | `engine/manifold_projection_core.md` | 0-2 |
| file | `engine/README.md` | 0 |
| file | `engine/seed_hydrogen_replication.py` | 0-2 |
| file | `engine/supernova_compiler_logic.md` | 0-2 |
| file | `grid/.gitignore` | 0 |
| file | `grid/eve_spatial_substrate.md` | 0-2 |
| file | `grid/fractal_coordinate_mapping.json` | 0-2 |
| file | `grid/README.md` | 0 |
| file | `kernel/.gitignore` | 0 |
| file | `kernel/executive_mode_switching.md` | 0-2 |
| file | `kernel/mashet_symbology.md` | 0-2 |
| file | `kernel/periodic_table_nodes.json` | 0-2 |
| file | `kernel/README.md` | 0 |
| file | `kernel/symbolic_judgement_engine.py` | 0-2 |
| file | `LICENSE` | 0 |
| file | `Link_to_Fractal_Grid_Code` | 1-2 |
| file | `LVT_Token_AI_Visialization_Instructions` | 1-2 |
| file | `Manifesto/00_preamble.md` | 0-2 |
| file | `Manifesto/01_lexical_sovereignty.md` | 0-2 |
| file | `Manifesto/02_spatial_fidelity.md` | 0-2 |
| file | `Manifesto/03_the_storage_paradigm.md` | 0-2 |
| file | `Manifesto/04_cognitive_liberty.md` | 0-2 |
| file | `Manifesto/99_tbd_universal_consensus.md` | 0-2 |
| file | `Manifold_Engine_MVP_Specs` | 1-2 |
| file | `math/.gitignore` | 0 |
| file | `math/constants_and_units.json` | 0-2 |
| file | `math/gravitational_collapse_logic.md` | 0-2 |
| file | `math/hydrogen_field_equations.md` | 0-2 |
| file | `math/manifold_projection_geometry.md` | 0-2 |
| file | `math/README.md` | 0 |
| file | `README.md` | 0-2 |
| file | `SentenceEngine.index.html` | 1-2 |
| file | `Tech_Spec` | 1-2 |
| file | `VISION.md` | 0-2 |
| folder | `contracts` | 0-2 |
| folder | `demo` | 0 |
| folder | `docs` | 0 |
| folder | `elemental_vault` | 1 |
| folder | `elemental_vault/web` | 1 |
| folder | `engine` | 0-2 |
| folder | `grid` | 0-2 |
| folder | `kernel` | 0-2 |
| folder | `Manifesto` | 0-2 |
| folder | `math` | 0-2 |

---

# Audit skills — interfaces

## 1. Verification protocol

Enumerate all current branch names and resolve tip commits. Compare every current source tree with the list above, excluding only root Contract000_Audit/**, which contains this maintenance circuit. The branch-key ranges are lossless: expand every integer between endpoints and map it to the named branch table. Compare folders, files and submodules, not only filenames in main. A changed tip requires inspecting whether its non-maintenance tree changed; a maintenance-only main commit does not invalidate unchanged source coverage. Record additions, renames, removals, type changes and unresolved/truncated trees. Never infer absence from access denial. Pin a coherent snapshot before reading.

## 2. Sequential file-by-file category audit

Resolve this represented branch through BRANCHES.json and enumerate every file assigned to its branch key. Read each file one at a time and retain the exact checkpoint. Scope: MCP tools/resources/prompts and API/event/schema/adapter connection contracts; distinguish designed interfaces from served endpoints. Identify architecturally specific keyterms and contextually definable interfaces. Inspect each distinct version; identical source blobs may reuse an explicit earlier reading record with every branch/path mapping retained. Archives require member-level coverage, not just the ZIP filename; binaries require format-appropriate inspection and honest limitations. Missing or unread content remains UNREAD/BLOCKED.

## 3. Accumulative translation record

Append discoveries to ../Contract000_interfaces.md with stable IDs, exact source pins, original contextual meaning, proposed MCP mapping, evidence, effects, dependencies and unresolved alternatives. Cross-reference other categories. A proposed translation is not an installed skill, available endpoint, authorization or verified outcome. Never copy private source text, credentials or protected archive data into public records.

## 4. Comparative branch analysis

Compare corresponding category accumulators at pinned revisions, and inspect their referenced implementations before merge recommendations. Publish a Consolidation and Integration Report issue in the receiving repository. Documentation consolidation precedes implementation integration; preserve differing alternatives and source provenance. Actual merges and test results are appended only after they occur.

## 5. Curator verification

Follow [000_CuratorVerification.md](000_CuratorVerification.md), update the list-only header from the reconciled snapshot, and preserve the earlier listing through Git history. Regenerate matching headers consistently across represented branch/category folders; do not falsely mark content read during directory refresh. Newly found source branches require new represented folders through maintenance authorization.

## 6. Final routing protocol

Return to the [maintenance README](Contract000_readme.md) and execute its final NEXT directory route with the saved checkpoint. Do not jump categories or silently restart an incomplete audit.
