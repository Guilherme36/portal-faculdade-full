#!/usr/bin/env python
import os
import subprocess

proto_dir = 'protos'
proto_files = [
    'student.proto',
    'teacher.proto',
    'subject.proto',
    'class.proto'
]

for proto_file in proto_files:
    proto_path = os.path.join(proto_dir, proto_file)
    print(f"Compilando {proto_path}...")
    
    subprocess.run([
        'python', '-m', 'grpc_tools.protoc',
        f'-I{proto_dir}',
        f'--python_out={proto_dir}',
        f'--grpc_python_out={proto_dir}',
        proto_path
    ])

print("Compilação concluída!")
