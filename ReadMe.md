# Dynamic TLS misconfiguration Detection#
Developed a framework that performs a comprehensive step by step dynamic and automated teardown of the app registration, login procedures and their SSL/TLS configurations to detect SSL/TLS vulnerabilities.

This contains the following 

reader.py : dpkt based pcap parser. 
out.pcap  : pcap file captured from Android Device 
parsed_pcap.txt : the output of the reader.py 


Instructions:  
run the reader as  
python2 reader.py out.pcap > parsed_pcap.txt  


