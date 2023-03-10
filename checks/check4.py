import subprocess
import re
import os

# pipenv run pytest -rA checks/check2.py -k 'test'

def testDockerfile():
    assert os.path.exists('ejemplo/Dockerfile')

def testRunDocker():
    result = subprocess.check_output(['./gradlew','clean','build'], cwd='ejemplo')
    result = subprocess.run(['docker', 'build','--tag=ejemplo:latest','.'], cwd='ejemplo').returncode
    assert result == 0
