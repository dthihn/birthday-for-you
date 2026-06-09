import glob
import re

html_files = glob.glob('noelnoem-main/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "const _tempInvMatrix" not in content:
        # 1. Add temp variables before class Particle
        content = re.sub(
            r'(class Particle \{)',
            r'// Optimization: Pre-allocate objects to prevent GC spikes in update loop\nconst _tempInvMatrix = new THREE.Matrix4();\nconst _tempFocusPos = new THREE.Vector3();\nconst _tempScale = new THREE.Vector3();\n\n\1',
            content
        )

        # 2. Replace focus target allocation
        # We need to capture the exact coordinates used in new THREE.Vector3(...)
        def focus_target_replace(match):
            coords = match.group(1)
            return f'_tempInvMatrix.copy(mainGroup.matrixWorld).invert();\n                        target = _tempFocusPos.set({coords}).applyMatrix4(_tempInvMatrix);'

        content = re.sub(
            r'const desiredWorldPos = new THREE\.Vector3\((.*?)\);\s*const invMatrix = new THREE\.Matrix4\(\)\.copy\(mainGroup\.matrixWorld\)\.invert\(\);\s*target = desiredWorldPos\.applyMatrix4\(invMatrix\);',
            focus_target_replace,
            content
        )

        # 3. Replace scale allocation
        content = re.sub(
            r'new THREE\.Vector3\(s,\s*s,\s*s\)',
            r'_tempScale.set(s, s, s)',
            content
        )

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Patched {file}")
