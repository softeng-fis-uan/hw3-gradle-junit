import subprocess
import re
import os

# pipenv run pytest -rA checks/check2.py -k 'test'

def testController():
    assert os.path.exists('ejemplo/src/main/java/co/edu/uan/sofeng/ejemplo/HelloController.java')

def testControllerTest():
    assert os.path.exists('ejemplo/src/test/java/co/edu/uan/sofeng/ejemplo/HelloControllerTest.java')

def testControllerIntegrationTest():
    assert os.path.exists('ejemplo/src/test/java/co/edu/uan/sofeng/ejemplo/HelloControllerIntegrationTest.java')

def testRunTests():
    result = subprocess.check_output(['./gradlew', 'test'], cwd='ejemplo').decode()
    print(result)
    assert re.search("BUILD SUCCESSFUL", result)

def testResults():
    assert os.path.exists('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerTest.xml')
    file = open('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerTest.xml',mode='r')
    results = file.read()
    file.close()
    properties = [
        'skipped="0"',
        'failures="0"'
        ]
    for p in properties:
        assert re.search(p, results)
    testsNumber = re.findall('tests="[0-9]+"', results)
    testsNumber = re.findall('[0-9]+', testsNumber[0])
    assert int(testsNumber[0]) >=1
    

def testIntegrationResults():
    assert os.path.exists('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerIntegrationTest.xml')
    file = open('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerIntegrationTest.xml',mode='r')
    results = file.read()
    file.close()
    properties = [
        'skipped="0"',
        'failures="0"'
        ]
    for p in properties:
        assert re.search(p, results)
    testsNumber = re.findall('tests="[0-9]+"', results)
    testsNumber = re.findall('[0-9]+', testsNumber[0])
    assert int(testsNumber[0]) >=1
