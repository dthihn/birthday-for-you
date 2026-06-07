
## 2024-05-18 - Reduce GC Pauses in THREE.js update loop
**Learning:** Instantiating new THREE.Vector3 and THREE.Matrix4 instances per particle per frame inside the `Particle.update` function creates excessive object allocations, leading to Garbage Collection (GC) pauses that degrade rendering frame rate and smoothness. This anti-pattern was present across all 14 HTML entry files.
**Action:** Extract short-lived object instantiation to shared module-level/global instances (`_tempScale`, `_tempInvMatrix`, `_tempWorldPos`) and use mutating methods (`.set()`, `.copy()`, `.applyMatrix4()`, `.lerp()`) instead.
