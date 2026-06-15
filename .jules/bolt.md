## 2026-06-15 - Reuse Vectors and Matrices in THREE.js Particle Update Loop
**Learning:** Found frequent allocations of `THREE.Vector3` and `THREE.Matrix4` inside `Particle.update()` loops across multiple similar HTML files, causing GC spikes and reduced framerates.
**Action:** Always create global reusable `_tempScale`, `_tempPos`, `_tempTarget`, and `_tempMatrix` objects instead of instantiating new ones every frame, and utilize `.set()`, `.copy()`, and `.applyMatrix4()` to modify these temporary structures without breaking other vector bindings in THREE.js.
