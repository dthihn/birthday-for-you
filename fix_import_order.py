import os
import glob
import re

def optimize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # We want to move the 3 _temp variables after the import statements
    # Pattern to match the 3 temp variables at the top of the script block
    pattern = r'(<script type="module">\s*)(const _tempScale = new THREE\.Vector3\(\);\s*const _tempTargetPos = new THREE\.Vector3\(\);\s*const _tempInvMatrix = new THREE\.Matrix4\(\);\s*)(import [^;]+;\s*import [^;]+;\s*import [^;]+;\s*)'

    replacement = r'\1\3\n        \2'

    content = re.sub(pattern, replacement, content)

    if content != original_content:
        print(f"Modified {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for filepath in glob.glob('noelnoem-main/*.html'):
    optimize_file(filepath)
