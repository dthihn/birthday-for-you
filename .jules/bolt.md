## 2024-05-17 - Prevent Garbage Collection Spikes in 3D Update Loops
**Learning:** Instantiating new objects (like `new THREE.Vector3`) inside high-frequency loops (like per-particle updates on every frame) causes massive garbage collection pauses and frame drops, especially noticeable with large particle counts.
**Action:** Use shared, module-level temporary objects (e.g., `const _tempScale = new THREE.Vector3()`) and methods that reuse instances (like `.set()` and `.copy()`) to prevent unnecessary allocations.
