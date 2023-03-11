import subprocess
import re
import os

# NO MODIFICAR ESTE ARCHIVO

def testDockerfile():
    assert os.path.exists('ejemplo/Dockerfile')

def testRunDocker():
    result = subprocess.check_output(['./gradlew','clean','build'], cwd='ejemplo')
    result = subprocess.run(['docker', 'build','--tag=ejemplo:latest','.'], cwd='ejemplo').returncode
    assert result == 0
