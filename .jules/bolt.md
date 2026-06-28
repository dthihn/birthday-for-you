## 2026-06-28 - Reusing Objects in THREE.js Render Loops
**Learning:** Instantiating `new THREE.Vector3()` or `new THREE.Matrix4()` inside the `Particle.update()` method per frame per particle creates significant garbage collection overhead, leading to visible stutter and memory spikes in WebGL animations.
**Action:** Always allocate temporary math objects at the module or class level (e.g., `_tempScale`, `_tempTarget`, `_tempMatrix`) and use mutation methods like `.set()`, `.copy()`, and `.applyMatrix4()` inside render loops to prevent GC allocation spikes.
