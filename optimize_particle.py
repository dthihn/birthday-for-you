import glob
import re

html_files = glob.glob('noelnoem-main/*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    modified = False
    if 'class Particle {' in content and 'new THREE.Vector3(s,s,s)' in content:
        if 'const _tempScale = new THREE.Vector3();' not in content:
            content = re.sub(
                r'class Particle \{',
                '// Optimization: Reusable objects to prevent GC spikes in update loop\n        const _tempScale = new THREE.Vector3();\n        const _tempWorldPos = new THREE.Vector3(0, 2, 38);\n        const _tempMatrix = new THREE.Matrix4();\n\n        class Particle {',
                content
            )
            modified = True

        if 'new THREE.Vector3(s,s,s)' in content:
            content = content.replace('new THREE.Vector3(s,s,s)', '_tempScale.set(s,s,s)')
            modified = True

        if 'const desiredWorldPos = new THREE.Vector3(0, 2, 38);' in content:
            content = content.replace('const desiredWorldPos = new THREE.Vector3(0, 2, 38);', '')
            modified = True

        if 'const invMatrix = new THREE.Matrix4().copy(mainGroup.matrixWorld).invert();' in content:
            content = content.replace('const invMatrix = new THREE.Matrix4().copy(mainGroup.matrixWorld).invert();', '_tempMatrix.copy(mainGroup.matrixWorld).invert();')
            modified = True

        if 'target = desiredWorldPos.applyMatrix4(invMatrix);' in content:
            content = content.replace('target = desiredWorldPos.applyMatrix4(invMatrix);', 'target = _tempWorldPos.set(0, 2, 38).applyMatrix4(_tempMatrix);')
            modified = True

        if modified:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")
