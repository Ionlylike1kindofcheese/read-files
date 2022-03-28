from time import sleep

file = open('README.md', 'r')

def fileread():
    line = True
    while line:
        line = file.readline()
        print(line)
        sleep(1)

fileread()

file.close()