import glob, re

files = glob.glob('noelnoem-main/*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
        if 'new THREE.Vector3(s,s,s)' in content:
            print(f, "has Vector3(s,s,s)")
        if 'new THREE.Matrix4().copy(mainGroup.matrixWorld).invert()' in content:
            print(f, "has Matrix4()")
