# open_port_scanner
A multi-threaded python port scanner built for identifying open ports and running services on a target system  

## **FEATURES**  
- multi-threaded scanning (one thread for each port)  
- common service detection  
- custom port ranges 1-65535 default scanning being 1-1024  
- automatically save results to a timestamped file  
  
## **LIBRARIES USED**  
- socket library for tcp/ip connection handling  
- threading library for concurrent port scanning  
- datetime library for timestamp generation  

---  
THE SCANNER RECOGNIZES 17 COMMON PORTS    
- 20  : FTP-data  
- 21  : FTP  
- 22  : SSH  
- 23  : Telnet  
- 25  : SMTP  
- 53  : DNS  
- 80  : HTTP  
- 110 : POP3  
- 143 : IMAP  
- 443 : HTTPS   
- 993 : IMAPS  
- 995 : POP3S  
- 3306: MySQL  
- 3389: RDP  
- 5432: PostgreSQL  
- 8080: HTTP-Proxy  
- 8443: HTTPS-Alt  

---  
## **SAMPLE OUTPUT**  
enter hostname or ip address to be scanned scanme.nmap.org  
45.33.32.156 was resolved for the input:scanme.nmap.org given  
enter start port 1  
enter end port 100  
SCANNING PORTS FROM 1 TO 100  
scanning started at  2026-05-12 12:43:16.444502  
NO OF OPEN PORTS FOUND: 2  
port no: 22 is open with service SSH  
port no: 80 is open with service HTTP  
