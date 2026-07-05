## 2024-10-31 - THREE.js Garbage Collection in Particle Updates
**Learning:** Instantiating `new THREE.Vector3()` and `new THREE.Matrix4()` inside high-frequency loops like `Particle.update()` (called thousands of times per frame) causes massive Garbage Collection spikes, leading to stuttering in the animation loop.
**Action:** Always hoist object instantiation outside of render/update loops. Use module-level cache variables and methods like `.set()`, `.copy()`, and `.applyMatrix4()` to modify them in place instead of creating new instances.
