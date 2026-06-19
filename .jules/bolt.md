## 2024-03-24 - THREE.js Object Instantiation in Update Loops
**Learning:** Instantiating new THREE.js objects (like `THREE.Vector3`, `THREE.Matrix4`) inside per-particle update loops (`Particle.update`) causes massive Garbage Collection (GC) spikes, degrading frame rates in WebGL applications.
**Action:** Declare shared module-level or global temporary objects (e.g., `_tempScale`, `_tempTarget`, `_invMatrix`) outside the class/update loop. Reuse them using methods like `.set()`, `.copy()`, and `.applyMatrix4()` to avoid GC pressure.
