## 2024-05-24 - Reduce GC Spikes in High-Frequency Loops
**Learning:** Re-instantiating `THREE.Vector3` or `THREE.Matrix4` inside a high-frequency loop (such as the `Particle.update` function called ~1500 times per frame) creates massive garbage collection overhead which causes frame drops and stuttering.
**Action:** Declare module-level or global temporary objects (`_tempScale`, `_tempTarget`, `_invMatrix`) and reuse them using `.set()`, `.copy()`, and `.applyMatrix4()` inside render/update loops instead of creating new instances.
