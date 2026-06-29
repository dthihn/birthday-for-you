## 2026-06-29 - [THREE.js GC Optimization]
**Learning:** Instantiating new THREE.js objects (like `THREE.Vector3` or `THREE.Matrix4`) inside high-frequency update loops (e.g., `Particle.update` running for hundreds of particles every frame) causes significant Garbage Collection (GC) spikes, degrading performance.
**Action:** When updating particle transformations, reuse module-level or global temporary objects using methods like `.set()`, `.copy()`, and `.applyMatrix4()` to avoid object instantiation overhead in the render loop.
