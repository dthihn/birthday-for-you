## 2024-05-15 - [GC Spikes in THREE.js Update Loops]
**Learning:** Found multiple places instantiating `new THREE.Vector3()` and `new THREE.Matrix4()` inside per-frame `update()` loops, causing significant GC overhead.
**Action:** Always pre-allocate reusable vectors/matrices (e.g., `_tempScale`, `_focusPos`, `_invMatrix`) outside the hot loop and use `.set()`, `.copy()`, and `.applyMatrix4()` to modify and apply them.
