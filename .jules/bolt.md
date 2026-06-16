## 2026-06-16 - Cache THREE.js objects to prevent GC spikes
**Learning:** Instantiating new objects (e.g. `new THREE.Vector3`) every frame for every particle causes excessive Garbage Collection spikes in high-frequency render loops.
**Action:** Declare module-level/global instances outside the update loop and use mutation methods like `.set()`, `.copy()`, or `.applyMatrix4()` to reuse those objects in performance-critical loops.
