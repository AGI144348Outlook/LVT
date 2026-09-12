# grid

The Fractal Grid substrate: `eve_spatial_substrate.md` describes the
Cartesian coordinate system shared by every LVT under the EVE wrapper, and
`fractal_coordinate_mapping.json` holds the recursive coordinate mapping data
that lets the Manifold Engine address a location from galactic to Planck
scale within one unified volume. The actual traversal/instancing code that
operates on this data lives in [engine/](../engine).
