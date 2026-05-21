import os
import glob
import re

html_files = glob.glob('noelnoem-main/*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    modified = False

    if "new THREE.Vector3(s,s,s)" in content:
        if "const _tempScale = new THREE.Vector3();" not in content:
            content = content.replace("class Particle {", "const _tempScale = new THREE.Vector3();\n        const _desiredWorldPos = new THREE.Vector3(0, 2, 38);\n        const _invMatrix = new THREE.Matrix4();\n        class Particle {")

        content = content.replace("new THREE.Vector3(s,s,s)", "_tempScale.set(s,s,s)")
        modified = True

    if "const desiredWorldPos = new THREE.Vector3(0, 2, 38);" in content:
        content = content.replace("const desiredWorldPos = new THREE.Vector3(0, 2, 38);", "")
        content = content.replace("const invMatrix = new THREE.Matrix4().copy(mainGroup.matrixWorld).invert();", "_invMatrix.copy(mainGroup.matrixWorld).invert();")
        content = content.replace("target = desiredWorldPos.applyMatrix4(invMatrix);", "target = _desiredWorldPos.set(0, 2, 38).applyMatrix4(_invMatrix);")
        modified = True

    if modified:
        with open(file, 'w') as f:
            f.write(content)

print("Done")
