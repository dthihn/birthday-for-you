## 2026-06-18 - Prevent GC Spikes in THREE.js Particle Loops
**Learning:** Instantiating new `THREE.Vector3` and `THREE.Matrix4` objects inside the `Particle.update()` loop that runs every frame for every particle causes significant Garbage Collection (GC) pressure and frame drops.
**Action:** Promote these to reusable file-scope variables (`_tempScale`, `_tempTarget`, `_tempMatrix`) and use `.set()`, `.copy()`, and `.applyMatrix4()` to update them in place instead of creating new instances.
