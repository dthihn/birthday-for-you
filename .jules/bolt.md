## 2024-07-04 - GC Spikes in High-Frequency Render Loops
**Learning:** Instantiating new objects (like `new THREE.Vector3` or `new THREE.Matrix4`) inside highly active methods like `Particle.update`, which run thousands of times per frame, causes severe Garbage Collection (GC) pauses and negatively impacts the frame rate.
**Action:** Always extract temporary object allocations into shared module-level or global constants and reuse them via methods like `.set()`, `.copy()`, and `.applyMatrix4()` inside render loops.
