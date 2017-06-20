#coding=utf-8
#!/usr/bin/python
import netifaces as ni
import ping
import os,sys

def pings(ip):
    result = ping.quiet_ping(ip, timeout=2, count=10, psize=64)
    if int(result[0]) == 100:
        os.system('systemctl restart flanneld')
    else:
        print "flannel is ok"
        sys.exit(1)

if __name__ == '__main__':
    ni.ifaddresses('docker0')
    ip = ni.ifaddresses('docker0')[2][0]['addr']
    pings(ip)
