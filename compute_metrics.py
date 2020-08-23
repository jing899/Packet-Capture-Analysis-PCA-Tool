from packet_parser import *

count = 1
    
def compute(f_list,host_ip,f,count):
    reqS = 0
    reqR = 0
    repS = 0
    repR = 0

    requestsSFrame = 0
    requestsRFrame = 0
    requestsSICMP = 0
    requestsRICMP = 0
    request_time = []
    reply_time = []
    first_time = []
    second_time = []
  

    countRtt = 0
    rd = 0
    countRd = 0
    hops = 0
    host = host_ip

    for element in f_list:
        #print element[0]
        if(element[4] == 'request') and (element[1] == host):
            reqS += 1
            repR += 1
            requestsSFrame += element[3]
            requestsSICMP += (element[3] / 2) - 42
            request_time.append(element[0])
            countRtt += 1
            
        elif(element[4] == 'reply') and (element[1] == host):
            reqR += 1
            repS += 1
            requestsRFrame += element[3] 
            requestsRICMP += (element[3] / 2) - 42
            second_time.append(element[0])
            countRd += 1

        elif(element[4] == 'reply'):
            reply_time.append(element[0])
            hops += 128 - element[6] + 1
        elif(element[4] == 'request') and (element[2] == host):
            first_time.append(element[0])
            
    dataSent = (requestsSFrame / 2 + requestsSICMP) 
    dataReceived = (requestsRFrame / 2 + requestsRICMP)
    rtt = sum([b-a for b,a in zip(reply_time,request_time)])
    rd = sum([m-n for m,n in zip(second_time,first_time)])
    avg_rd = (rd / countRd )*1000000
    avg_rtt = (rtt /countRtt) * 1000
    through_put = requestsSFrame / rtt / 1000
    good_put = dataSent / rtt / 1000
    avg_hops = float(hops) / float(countRtt)
    
    f.write('Node ' + str(count) + '\n')
    f.write('\n')
    f.write('Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received\n')
    f.write(str(reqS) + ',' + str(reqR) + ',' + str(repS) + ',' + str(repR) + '\n')
    f.write('Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)\n')
    f.write(str(requestsSFrame) + ',' + str(dataSent) + '\n')
    f.write('Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)\n')
    f.write(str(requestsRFrame) + ',' + str(dataReceived) + '\n')
    f.write('\n')
    f.write('Average RTT (milliseconds),' + str(avg_rtt) + '\n')
    f.write('Echo Request Throughput (kB/sec),' + str(through_put) + '\n')
    f.write('Echo Request Goodput (kB/sec),' + str(good_put) + '\n')
    f.write('Average Reply Delay (microseconds),' + str(avg_rd) + '\n')
    f.write('Average Echo Request Hop Count,' + str(avg_hops) + '\n')
    f.write('\n')
 

    
# COMPUTE
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



