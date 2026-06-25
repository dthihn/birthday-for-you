## 2024-03-21 - [Prevent GC Spikes in THREE.js]
 **Learning:** Instantiating new THREE.js objects (like `new THREE.Vector3()`) inside high-frequency update loops (e.g., Particle updates per frame) causes significant Garbage Collection (GC) spikes, leading to stuttering in the animation.
 **Action:** To prevent these spikes, reuse module-level or global temporary objects (e.g., `const _tempScale = new THREE.Vector3();`) and use methods like `.set()`, `.copy()`, and `.applyMatrix4()` to modify them in place instead of creating new instances.
