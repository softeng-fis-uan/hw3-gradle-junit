import subprocess
import re
import os

# check project folder: : pipenv run pytest -rA checks/check1.py -k 'testFiles'
def testFiles():
    assert os.path.exists('ejemplo')
    assert os.path.exists('ejemplo/gradlew')

# check project properties: pipenv run pytest -rA checks/check1.py -k 'testProjectMetadata'
def testProjectMetadata():
    file = open('ejemplo/build.gradle',mode='r')
    build = file.read()
    file.close()
    properties = [
        "group = 'co.edu.uan.sofeng.ejemplo'", 
        "sourceCompatibility = '17'",
        "org.springframework.boot:spring-boot-starter-data-jpa",
	    "org.springframework.boot:spring-boot-starter-web",
        ]
    for p in properties:
        assert re.search(p, build)

# check gradle: pipenv run pytest -rA checks/check1.py -k 'testGradle'
def testGradle():
    result = subprocess.check_output(['./gradlew'], cwd='ejemplo').decode()
    print(result)
    assert re.search("Welcome to Gradle", result)
