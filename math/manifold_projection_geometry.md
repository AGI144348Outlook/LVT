# Manifold Projection Math

## 1. The UV-to-XYZ Mapping
A coordinate $(u, v)$ on the unfolded sphere surface is transformed into a 3D volume $V$ via:

$$V(u, v, z) = \int_{z_{min}}^{z_{max}} \text{Manifold}(u, v) dz$$

## 2. Depth Resolution
The Z-axis resolution is tied to the **Fractal Grid** depth constant ($D$):
$$\text{Resolution} = \text{Base_Scale} \times 2^{-D}$$

This allows the Hydrogen Seed to maintain Planck-scale precision ($10^{-35}$) locally, while the EVE environment remains at a macro-scale resolution.
