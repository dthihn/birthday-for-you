## 2026-06-24 - Eliminate GC Spikes in High-Frequency THREE.js Render Loops
**Learning:** Instantiating new objects (like `THREE.Vector3` or `THREE.Matrix4`) per particle every frame in `Particle.update()` creates enormous GC pressure in THREE.js applications (e.g. 4000 particles * 60 FPS = 240,000 objects/sec).
**Action:** When updating particle transformations, always inject and reuse module-level or global temporary objects (`_tempScale`, `_tempTarget`, `_tempInvMatrix`) using mutating methods like `.set()`, `.copy()`, and `.applyMatrix4()` instead of the `new` keyword.
