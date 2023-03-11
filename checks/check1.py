import subprocess
import re
import os

# NO MODIFICAR ESTE ARCHIVO

def testFiles():
    assert os.path.exists('ejemplo')
    assert os.path.exists('ejemplo/gradlew')

def testProjectMetadata():
    file = open('ejemplo/build.gradle',mode='r')
    build = file.read()
    file.close()
    properties = [
        "group = 'co.edu.uan.sofeng'", 
        "sourceCompatibility = '17'",
        "org.springframework.boot:spring-boot-starter-data-jpa",
	    "org.springframework.boot:spring-boot-starter-web",
        ]
    for p in properties:
        assert re.search(p, build)

def testGradle():
    result = subprocess.check_output(['./gradlew'], cwd='ejemplo').decode()
    print(result)
    assert re.search("Welcome to Gradle", result)
