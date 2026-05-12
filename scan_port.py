import socket
import threading
from datetime import datetime

common_ports = {
    20: "FTP-data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt"
}

def scan_port(host,port,openports):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        print(f'checking port no:{port}')
        result=sock.connect_ex((host,port))
        if(result==0):
            desc=common_ports.get(port,'unknown')
            print('port no:',port,'using service',desc,'is open')
            openports.append([port,desc])
        elif(port!=end):
            print('...moving onto next...')
        sock.close()
    except:
        pass

def scan_ports(host,startport,endport):
    print(f'SCANNING PORTS FROM {startport} TO {endport}')
    print('scanning started at ',datetime.now())
    openports=[]
    threads=[]
    for i in range(startport,endport+1):
        port=i
        thread=threading.Thread(target=scan_port,args=(host,port,openports))
        threads.append(thread)
        thread.start()
        for i in threads:
            thread.join()
    print('-'*20)
    print(f'NO OF OPEN PORTS FOUND: {len(openports)}')
    print('-'*20)
    if openports:
        for x in openports:
            print(f'port no: {x[0]} is open with service {x[1]}')
        file1=f"scan_result_of_{host}_at_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(file1,'w') as file1:
            file1.write(f'NO OF OPEN PORTS FOUND: {len(openports)}\n')
            for x in openports:
                file1.write(f'port no: {x[0]} is open with service {x[1]}\n')
        print('file writing successful')
    else:
        print('no open ports found')

hostinput=input('enter hostname or ip address to be scanned ')
try:
    ipaddr=socket.gethostbyname(hostinput)
    print(f'{ipaddr} was resolved for the input:{hostinput} given')
except:
    print('could not resolve ip address')
    exit(0)
start=int(input('enter start port ')or "1")
end=int(input('enter end port ')or "1024")
if(start<1 or end>65535 or end<start):
    print('invalid entry for port numbers pls try again')
scan_ports(ipaddr,start,end)

