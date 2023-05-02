from netaddr import *
from run import range_list


iplist = []
for iprange in range_list:

    for ip in IPNetwork(iprange):
        iplist.append(id)
        
print(len(iplist))
