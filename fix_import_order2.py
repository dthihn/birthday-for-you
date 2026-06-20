import os
import glob
import re

def optimize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove the existing temp variables that might be in the middle of imports
    content = re.sub(r'\s*const _tempScale = new THREE\.Vector3\(\);\s*const _tempTargetPos = new THREE\.Vector3\(\);\s*const _tempInvMatrix = new THREE\.Matrix4\(\);', '', content)

    # Find the last import statement and insert the variables after it
    # We can match all imports
    import_block_end = content.rfind('import { GLTFLoader }')
    if import_block_end != -1:
        # Find end of this line
        end_of_line = content.find('\n', import_block_end)
        content = content[:end_of_line] + '\n\n        const _tempScale = new THREE.Vector3();\n        const _tempTargetPos = new THREE.Vector3();\n        const _tempInvMatrix = new THREE.Matrix4();' + content[end_of_line:]
    else:
        print(f"GLTFLoader not found in {filepath}")

    if content != original_content:
        print(f"Modified {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for filepath in glob.glob('noelnoem-main/*.html'):
    optimize_file(filepath)
