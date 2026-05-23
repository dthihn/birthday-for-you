## 2024-03-24 - [Memory] Pre-allocate objects in render loop
**Learning:** Using `new THREE.Vector3()` or `new THREE.Matrix4()` inside a `requestAnimationFrame` update loop for particles creates severe Garbage Collection spikes because thousands of objects are allocated per frame (e.g. 1500 particles * 60 FPS = 90,000 vectors/sec).
**Action:** Always pre-allocate `THREE.Vector3` and `THREE.Matrix4` as module-level constants and reuse them via `.copy()` and `.set()` in update loops.
