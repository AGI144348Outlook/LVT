# contracts

Solidity source for the LVT-EVE on-chain layer: the ERC-1155-based
`LVT_1155_Nested_Standard` token, which implements the nested "Morphological
Seed" ownership model described in the [Tech Spec](../docs/tech-spec.md), and
the `EVE_Environment_Wrapper`, the shared coordinate anchor that lets separate
LVTs resolve a common spatial reality. `file_provenanve_protocol.md` documents
how on-chain provenance is tied back to this repository's Git history. This
directory currently holds only the reference implementation; a Hardhat or
Foundry project (tests, deployment scripts, network config) has not yet been
set up here.
