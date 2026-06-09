import glob
import re
import os

html_files = glob.glob('noelnoem-main/*.html')
print(f"Found {len(html_files)} HTML files.")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if 'class Particle' exists
    if 'class Particle {' in content:
        print(f"File {file} has Particle class.")
