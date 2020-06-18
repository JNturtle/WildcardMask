# input IP Address
ips =  [[192,168,0,0],[192,168,0,1],[192,168,0,2],[192,168,0,3],[192,168,0,4],[192,168,0,12]]
from collections import defaultdict
wc = defaultdict(list)

def check(strIP, strIP2):
    dismatch = 0
    pos = -1
    for i in range(32):
        if strIP[i] != strIP2[i]:
            if strIP[i] == "*" or strIP2[i] == "*": return -1
            dismatch += 1
            pos = i
            if dismatch == 2: return -1
    return pos

for ip in ips:
    strIP = "{:0>8}{:0>8}{:0>8}{:0>8}".format(*[bin(num)[2:] for num in ip])
    level = 0
    pos = 0
    while pos != -1 and wc[level]:        
        for j in range(len(wc[level])):
            pos = check(strIP, wc[level][j][1])
            if not pos == -1:
                ip = wc[level].pop(j)[0]
                strIP = strIP[:pos] + "*" + strIP[pos+1:]
                level += 1
                break         
    wc[level].append([ip, strIP])
    
result = []
for key in wc:
    for NW in wc[key]:
        NW[1] = NW[1].replace("1", "0").replace("*", "1")
        result.append([NW[0], [int(NW[1][0:8],2), int(NW[1][8:16],2),int(NW[1][16:24],2),int(NW[1][24:32],2)]])

# Convert format
for each in sorted(result):
    Network = ".".join([str(num) for num in each[0]]) 
    WildcardMask = ".".join([str(num) for num in each[1]]) 
    print("Network: {:}, Wildcard Mask: {:}".format(Network, WildcardMask))
    
# => Network: 192.168.0.0, Wildcard Mask: 0.0.0.3
# => Network: 192.168.0.4, Wildcard Mask: 0.0.0.8
