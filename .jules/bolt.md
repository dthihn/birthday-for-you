## 2024-05-24 - Avoid THREE.js Object Instantiation in Render Loops
**Learning:** Instantiating `new THREE.Vector3()` or `new THREE.Matrix4()` inside the `requestAnimationFrame` update loop (especially for thousands of particles) causes massive Garbage Collection spikes that drop framerates significantly.
**Action:** Always declare reusable temporary objects (e.g., `_tempScale = new THREE.Vector3()`) at the module scope and use `.set()`, `.copy()`, and `.applyMatrix4()` to mutate them in-place within update loops.
