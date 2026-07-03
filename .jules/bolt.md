## 2024-05-24 - Avoid THREE.js Object Instantiation in Render Loop
**Learning:** Instantiating new THREE.js objects (like `new THREE.Vector3()`, `new THREE.Matrix4()`) inside `update` loops for particles or animation loops creates unnecessary garbage collection spikes, significantly impacting performance and causing stutters.
**Action:** Declare reusable variables (`_tempDesiredWorldPos`, `_tempInvMatrix`, `_tempScale`) outside the class or update function, and use their mutation methods (`.set()`, `.copy()`, `.invert()`, `.applyMatrix4()`) instead of instantiating new objects.
