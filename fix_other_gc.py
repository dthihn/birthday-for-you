import os
import glob

html_files = glob.glob('noelnoem-main/*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    modified = False

    if "new THREE.Vector3(" in content:
        # Avoid matching places we already fixed or actual static constants
        # Search for instances inside loops or frequently called functions
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "new THREE.Vector3(" in line and "spinSpeed" not in line and "posTree =" not in line and "posScatter =" not in line:
                pass # print(f"{file}:{i} - {line.strip()}")

print("Done checking")
