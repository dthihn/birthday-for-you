## 2026-07-02 - [Reuse THREE.js objects in update loop]
**Learning:** In high-frequency functions like THREE.js render/update loops, creating new instances of classes like `THREE.Vector3` or `THREE.Matrix4` per frame per particle causes significant Garbage Collection (GC) spikes, degrading frame rate.
**Action:** Inject and reuse module-level global objects (e.g., `_tempScale`, `_tempTarget`, `_invMatrix`) using mutating methods like `.set()`, `.copy()`, and `.applyMatrix4()` instead of instantiating new objects in every `update()` call.
