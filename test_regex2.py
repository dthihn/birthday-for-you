import glob
import re

html_files = glob.glob('noelnoem-main/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const desiredWorldPos = new THREE\.Vector3\((.*?)\);', content)
    if match:
        print(f"{file}: {match.group(1)}")
    else:
        print(f"{file}: NOT FOUND")
