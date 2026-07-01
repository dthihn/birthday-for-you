## 2024-05-24 - Object Reuse in THREE.js Render Loops
**Learning:** Instantiating new objects (e.g., `new THREE.Vector3()`, `new THREE.Matrix4()`) within high-frequency update loops like `Particle.update` across a large particle system causes significant Garbage Collection (GC) spikes, degrading frame rates and overall performance.
**Action:** Always declare module-scoped or global temporary objects (e.g., `_tempScale`, `_tempTarget`, `_tempMatrix`) outside the render loop and reuse them using in-place mutators like `.set()`, `.copy()`, and `.applyMatrix4()` when working with THREE.js.
