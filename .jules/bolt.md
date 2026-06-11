## 2024-06-11 - Prevent Garbage Collection in THREE.js hot loops
**Learning:** Instantiating `new THREE.Vector3` or `new THREE.Matrix4` inside `requestAnimationFrame` update loops (especially per particle) causes severe Garbage Collection (GC) spikes, degrading framerate.
**Action:** Declare reusable global or module-level variables (e.g. `const _tempScale = new THREE.Vector3()`) and mutate them using `.set()`, `.copy()`, and `.applyMatrix4()` inside the hot loop instead of allocating new memory every frame.
