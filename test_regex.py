import re

content = """
                else if (mode === 'FOCUS') {
                    if (this.mesh === focusTargetMesh) {
                        const desiredWorldPos = new THREE.Vector3(0, 2, 38);
                        const invMatrix = new THREE.Matrix4().copy(mainGroup.matrixWorld).invert();
                        target = desiredWorldPos.applyMatrix4(invMatrix);
                    } else target = this.posScatter;
                }
"""

focus_target_search = r'const desiredWorldPos = new THREE\.Vector3\([0-9\., ]+\);\s*const invMatrix = new THREE\.Matrix4\(\)\.copy\(mainGroup\.matrixWorld\)\.invert\(\);\s*target = desiredWorldPos\.applyMatrix4\(invMatrix\);'
focus_target_replace = r'_tempInvMatrix.copy(mainGroup.matrixWorld).invert();\n                        target = _tempFocusPos.set(0, 2, 38).applyMatrix4(_tempInvMatrix);'
new_content = re.sub(focus_target_search, focus_target_replace, content)

print("Changed:", new_content != content)
print(new_content)
