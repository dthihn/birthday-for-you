## 2024-05-24 - [Avoid new THREE.Vector3 per frame]
**Learning:** Found multiple places in `Particle.update` where `new THREE.Vector3(s,s,s)` and `new THREE.Matrix4().copy(...)` were called on every frame for thousands of particles. This triggers massive Garbage Collection (GC) spikes, causing stuttering and dropping frame rates.
**Action:** Extract temporary vector and matrix objects to global scope (`const _tempScale = new THREE.Vector3(); const _invMatrix = new THREE.Matrix4();`) and use `.set(s,s,s)` and `.copy().invert()` on the same object to avoid allocation on hot paths.
