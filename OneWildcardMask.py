# input IP Address
# ips : [[a1,a2,a3,a4], [b1,b2,b3,b4], ...]
ips = [[192.168.0.4], [192.168.0.12]]

wc = [[[0,0,0,0], [255,255,255,255]]] # default WildcardMask
if ips:
    wc = [[ips.pop(0), [0,0,0,0]]]
    for ip in ips:
        for i in range(4):
            wc[0][1][i] |= wc[0][0][i] ^ ip[i]

# output the result
print(wc) 
# => [[192.168.0.4],[0,0,0,8]]
