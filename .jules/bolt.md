## 2026-06-23 - Reuse THREE.js Objects to Prevent GC Spikes
**Learning:** High-frequency rendering loops (e.g., `Particle.update`) that repeatedly instantiate objects like `new THREE.Vector3` or `new THREE.Matrix4` cause significant Garbage Collection (GC) pressure, leading to frame drops or stutters in THREE.js scenes.
**Action:** When working on particle systems or anything within a `requestAnimationFrame` loop, always declare global or module-level reusable objects (e.g., `_tempVec.set(x, y, z)`) to hold intermediate values and avoid allocating new objects per frame.
