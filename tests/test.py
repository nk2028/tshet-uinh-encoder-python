import os
import subprocess
import sys

base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TshetUinhEncoder')

python_files = []
for dirpath, dirnames, filenames in os.walk(base_directory):
    for file in filenames:
        if file.endswith('.py'):
            full_path = os.path.join(dirpath, file)
            python_files.append(full_path)

for file in python_files:
    process = subprocess.run([sys.executable, file])
    return_code = process.returncode
    if return_code != 0:
        exit(return_code)
