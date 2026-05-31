## 2026-05-31 - THREE.js Garbage Collection Spikes in Particle Update Loops
**Learning:** Frequent object instantiation (`new THREE.Vector3()`, `new THREE.Matrix4()`) inside high-frequency update loops (like `Particle.prototype.update` which runs 4000+ times per frame) causes massive GC spikes, leading to stuttering and FPS drops.
**Action:** Always pre-allocate module-level or global temporary objects (`_tempScale`, `_tempTarget`, `_invMatrix`) and reuse them using methods like `.set()`, `.copy()`, and `.applyMatrix4()` inside render loops to achieve zero-allocation per frame.
