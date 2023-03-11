import subprocess
import re
import os

# NO MODIFICAR ESTE ARCHIVO

def testSayHello():
    file = open('ejemplo/src/main/java/co/edu/uan/sofeng/ejemplo/HelloController.java',mode='r')
    source = file.read()
    file.close()
    properties = [
        'String sayHello'
        ]
    for p in properties:
        assert re.search(p, source)

def testSayHelloTest():
    file = open('ejemplo/src/test/java/co/edu/uan/sofeng/ejemplo/HelloControllerTests.java',mode='r')
    source = file.read()
    file.close()
    properties = [
        'sayHello()'
        ]
    for p in properties:
        assert re.search(p, source)

def testSayHelloParam():
    file = open('ejemplo/src/main/java/co/edu/uan/sofeng/ejemplo/HelloController.java',mode='r')
    source = file.read()
    file.close()
    properties = [
        'RequestParam'
        ]
    for p in properties:
        assert re.search(p, source)


def testSayHelloParamTest():
    file = open('ejemplo/src/test/java/co/edu/uan/sofeng/ejemplo/HelloControllerTests.java',mode='r')
    source = file.read()
    file.close()
    properties = [
        'sayHelloName()'
        ]
    for p in properties:
        assert re.search(p, source)


def testRunTests():
    result = subprocess.check_output(['./gradlew', 'test'], cwd='ejemplo').decode()
    print(result)
    assert re.search("BUILD SUCCESSFUL", result)

def testResults():
    assert os.path.exists('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerTests.xml')
    file = open('ejemplo/build/test-results/test/TEST-co.edu.uan.sofeng.ejemplo.HelloControllerTests.xml',mode='r')
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
    assert int(testsNumber[0]) >=3
