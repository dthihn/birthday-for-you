import os
import glob

html_files = glob.glob('noelnoem-main/*.html')

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    if "new THREE.Vector3(s,s,s)" in content:
        if "const tempScale = new THREE.Vector3();" not in content:
            content = content.replace("class Particle {", "const tempScale = new THREE.Vector3();\n        class Particle {")

        content = content.replace("new THREE.Vector3(s,s,s)", "tempScale.set(s,s,s)")

        with open(file, 'w') as f:
            f.write(content)

print("Done")
