import glob
import re

html_files = glob.glob('noelnoem-main/*.html')
for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
        if 'new THREE.Vector3(s,s,s)' in content:
            print(f"File {f} matches!")
