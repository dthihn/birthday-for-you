## 2024-06-21 - [Prevent GC Spikes in THREE.js]
**Learning:** In high-frequency render loops (like THREE.js Particle systems), instantiating new objects (e.g., `new THREE.Vector3()` or `new THREE.Matrix4()`) per frame per particle creates massive Garbage Collection (GC) spikes that degrade performance and cause stuttering.
**Action:** Always reuse global or module-level objects (`_tempScale`, `_tempTarget`, `_invMatrix`) using methods like `.set()`, `.copy()`, and `.applyMatrix4()` to avoid continuous memory allocation in the `update(dt)` loop.
