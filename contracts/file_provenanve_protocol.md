# Provenance Handshake Protocol
**Role:** Validating the "Seriousness" of the Token.

## 1. The Git-Hash Anchor
Every LVT minted via the `LVTEveStandard` contract must include a **Git Commit Hash**. 
- This hash points to the exact version of the **Manifold Engine** used to generate the token's data.
- It ensures that the "Storage" or "Spatial" fidelity of the token is backed by the open-source (or private-provenance) code in this repository.

## 2. Multi-Purpose Licensing
Holders of the LVT gain the rights to execute the Manifold Engine across all three modes (Lexical, Spatial, Storage) within their own private **EVE Substrate**.
