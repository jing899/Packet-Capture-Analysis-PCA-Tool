from filter_packets import *
from packet_parser import *
from compute_metrics import *

# FILTER
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

# PARSER
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

# COMPUTE
count=1
file='Mini Project 2 Output.txt'
f=open(file, 'w')
    
host_ipA = '192.168.100.1'
host_ipB = '192.168.100.2'
host_ipC = '192.168.200.1'
host_ipD = '192.168.200.2'

compute(A,host_ipA,f,count)
count=count+1
compute(B,host_ipB,f,count)
count=count+1
compute(C,host_ipC,f,count)
count=count+1
compute(D,host_ipD,f,count)

f.close()













