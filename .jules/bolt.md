
## 2024-06-13 - [Fix GC Spikes in THREE.js Render Loop]
 **Learning:** In high-frequency functions like `THREE.js` render/update loops, creating new objects per frame (e.g., `new THREE.Vector3`, `new THREE.Matrix4`) causes Garbage Collection (GC) spikes, degrading performance.
 **Action:** Reuse module-level or global objects using methods like `.set()`, `.copy()`, and `.applyMatrix4()` instead of instantiating new objects for every particle or frame.
