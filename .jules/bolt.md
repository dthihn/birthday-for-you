## 2026-06-03 - Reuse THREE.js Objects in Render Loop
**Learning:** Instantiating new THREE.js objects (like `new THREE.Vector3` or `new THREE.Matrix4`) inside a particle update loop (called 60 times a second for 4000+ particles) causes severe Garbage Collection (GC) spikes, leading to frame stutters.
**Action:** Extract these objects to global space (e.g., `_tempScale`, `_tempMatrix`) and mutate them in place using methods like `.set()`, `.copy()`, and `.applyMatrix4()` inside the render loop to eliminate per-frame memory allocations.
