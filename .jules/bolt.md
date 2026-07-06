## 2024-06-25 - Object Pool Anti-pattern in Particle System
**Learning:** The Three.js application instantiates new `THREE.Vector3` and `THREE.Matrix4` objects directly inside the `Particle.update()` method. Since this method is called per-particle per-frame (e.g., 1500 particles * 60 FPS = 90,000 allocations/sec), it causes severe Garbage Collection spikes and stuttering.
**Action:** Always hoist commonly used temporary Vector/Matrix objects to module/global scope and reuse them using `.set()`, `.copy()`, and `.applyMatrix4()` in hot loops instead of `new`.
