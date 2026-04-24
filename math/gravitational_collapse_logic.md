# Gravitational Collapse & Stellar Ignition Logic

## 1. The Jeans Mass Threshold ($M_j$)
The Manifold Engine monitors the instancing count ($N$) within the Hydrogen Square. When the total mass $M$ exceeds the Jeans Mass, the "Stellar Forge" compiler is activated:

$$M_j \approx \left( \frac{5kT}{G\mu m_H} \right)^{3/2} \left( \frac{3}{4\pi\rho} \right)^{1/2}$$

## 2. Nucleosynthesis Metadata
Once ignition occurs, the LVT updates its internal metadata to shift from a "Gas Cloud State" to a "Fusion State." This begins the automated populating of:
- **Helium Tokens:** $4^1 H \to ^4 He + 2e^+ + 2\nu_e + \gamma$
- **Heavy Element Tokens:** Triggered at the Iron ($Fe$) limit during the Supernova phase.
