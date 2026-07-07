import glob, re

files = glob.glob('noelnoem-main/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Add the globals before `class Particle {`
    if 'const _tempScale = new THREE.Vector3();' not in content:
        content = content.replace(
            'class Particle {',
            '// Optimization: Reuse THREE objects to prevent GC spikes in update loop\n        const _tempScale = new THREE.Vector3();\n        const _desiredWorldPos = new THREE.Vector3(0, 2, 38);\n        const _invMatrix = new THREE.Matrix4();\n        const _tempTarget = new THREE.Vector3();\n\n        class Particle {'
        )

    # Replace new THREE.Vector3(s,s,s)
    content = content.replace(
        'this.mesh.scale.lerp(new THREE.Vector3(s,s,s), 4*dt);',
        'this.mesh.scale.lerp(_tempScale.set(s,s,s), 4*dt);'
    )

    # Replace desiredWorldPos and invMatrix logic
    old_focus_logic = '''                        const desiredWorldPos = new THREE.Vector3(0, 2, 38);
                        const invMatrix = new THREE.Matrix4().copy(mainGroup.matrixWorld).invert();
                        target = desiredWorldPos.applyMatrix4(invMatrix);'''
    new_focus_logic = '''                        _invMatrix.copy(mainGroup.matrixWorld).invert();
                        target = _tempTarget.copy(_desiredWorldPos).applyMatrix4(_invMatrix);'''
    content = content.replace(old_focus_logic, new_focus_logic)

    with open(filepath, 'w') as f:
        f.write(content)
print("Updated all files")
