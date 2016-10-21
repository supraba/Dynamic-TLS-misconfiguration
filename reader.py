#!/usr/bin/env python

import dpkt
import sys
import socket

f = open(sys.argv[1], "r")
pcap = dpkt.pcap.Reader(f)

http_ports = [80, 8080, 443] # Add other ports if you website on non-standard port.
urls = [ ]
headers = [ ]

for timestamp, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    dst_ip_addr_str = socket.inet_ntoa(ip.dst)

    if tcp.__class__.__name__ == 'TCP':
        if tcp.dport in http_ports and len(tcp.data) > 0:
            try:
                http = dpkt.http.Request(tcp.data)
                #urls.append("HOST:" + http.headers['host'] +"\nURI:" + http.uri + "\nuseragent:" + http.headers['user-agent'])
                print('==');
                for x in http.headers:
                    print(x , ':' , http.headers[x]) 
                print('URI:' ,http.uri)
                print('PORT:',tcp.dport)
                print('IP:',dst_ip_addr_str)

            except Exception as e:
                continue
f.close()

#print "[+] URLs extracted from PCAP file are:\n"
#for url in urls:
#    print url
