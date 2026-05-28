## 2024-12-25 - Object Creation in THREE.js Render Loop
**Learning:** Instantiating new objects (e.g. `new THREE.Vector3()`, `new THREE.Matrix4()`) within high-frequency loops like `Particle.update()` (called thousands of times per frame) causes massive Garbage Collection (GC) spikes leading to frame drops in Three.js applications.
**Action:** Always declare module-level or global temporary objects (e.g., `_tempScale`, `_invMatrix`) and reuse them using `.set()`, `.copy()`, and `.applyMatrix4()` inside render/update loops.
