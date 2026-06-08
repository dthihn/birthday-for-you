## 2024-05-24 - Object Allocation in Render Loop
**Learning:** Creating new THREE.js objects (like Vector3, Matrix4) inside `update` loops for thousands of particles causes severe Garbage Collection (GC) spikes and frame rate drops.
**Action:** Always use module-level or global temporary objects (`_tempScale.set(s,s,s)`) instead of `new THREE.Vector3(s,s,s)` inside high-frequency loops.
