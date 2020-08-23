import sys,string,os

def filter(filename):

    file_data =[]
    f = open(filename + '.txt' ,'r')
    line = f.readline()

    previousLine = ""
    for line in f:
        if(("reply" in line) or ("request" in line)):
            file_data.append(previousLine)
            file_data.append(line)
        previousLine = line
    f.close()


    i = 1
    while os.path.exists("Node%s_filtered.txt" % i):
        i += 1
    with open(filename + "_filtered.txt", "w") as fi:
        for element in file_data:
            fi.write("%s\n" % element)
    f.close()

fileA = 'Node1'
fileB = 'Node2'
fileC = 'Node3'
fileD = 'Node4'
fileE = 'Node5'
filter(fileA) 
filter(fileB) 
filter(fileC) 
filter(fileD) 
filter(fileE)

