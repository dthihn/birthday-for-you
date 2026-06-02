## 2026-06-02 - Object Allocation in Particle update loops
**Learning:** Instantiating `new THREE.Vector3` or `new THREE.Matrix4` in high-frequency update loops (like the `update` method of a `Particle` class that is called for 1000s of particles every frame) causes significant Garbage Collection (GC) spikes, degrading frame rate.
**Action:** Declare reusable module-level variables (e.g., `_tempScaleVector`, `_tempFocusVector`, `_tempMatrix`) and use `.set()`, `.copy()`, and `.applyMatrix4()` to mutate them in-place instead of creating new objects per frame/particle.
