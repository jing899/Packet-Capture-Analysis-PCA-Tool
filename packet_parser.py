L = []

def parse(filename,L):
    f = open(filename,'r')
    line = f.readline()
    packet = []
    flag = False
    

    for line in open(filename):

        if "No." in line:
            flag = True
            continue
        if flag:
            line = line.split("\n")
            for v in line:
                if len(v.strip()) > 0:
                    v = v.strip().split()
                    packet.append(float(v[1]))
                    packet.append(v[2])
                    packet.append(v[3])
                    packet.append(int(v[5]))
                    packet.append(v[8])
                    packet.append(int(v[10].split("=")[1].split("/")[0]))
                    packet.append(int(v[11].split("=")[1]))
    
    #print packet


    for i in range(0,len(packet),7):
        L.append(packet[i:i+7])
    #print L
    

A = []
B = []
C = []
D = []
E = []

fileA = 'Node1_filtered.txt'
fileB = 'Node2_filtered.txt'
fileC = 'Node3_filtered.txt'
fileD = 'Node4_filtered.txt'
fileE = 'Node5_filtered.txt'

parse(fileA,A)
#print A
parse(fileB,B)
#print B
parse(fileC,C)
#print C
parse(fileD,D)
#print D
parse(fileE,E)
#print E

