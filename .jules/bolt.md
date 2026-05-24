## 2024-05-24 - Prevent GC Spikes in THREE.js Render Loop
**Learning:** Instantiating new objects (e.g., `new THREE.Vector3()`, `new THREE.Matrix4()`) inside update loops like `Particle.update()` (which runs every frame for 1500+ particles) causes severe Garbage Collection (GC) spikes, leading to frame drops.
**Action:** Always pre-allocate reusable, module-level variables (e.g., `_desiredWorldPos = new THREE.Vector3()`) and use their `.set()`, `.copy()`, and `.applyMatrix4()` methods instead of instantiating new objects per frame/particle.
