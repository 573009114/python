#!/usr/bin/env python2.6
# -*- coding: utf-8 -*
import os
import sys
import paramiko

import getpass

Host=['10.15.203.19','10.15.203.18','10.15.203.34']



Command=raw_input("input command: ")
 
print "#" *60
 
for h in Host:
    try:
    	ssh = paramiko.SSHClient()
    	ssh.load_system_host_keys()
    	ssh.connect(h,22,"root")
       	stdin, stdout, stderr = ssh.exec_command(Command)
	fo = open("tmp.txt", "a")
	fo.write(h +'\n' + stdout.read())
	fo.close()
	print 'program completed. please open tmp.txt.'
    except Exception:
	print '%s unable to log or other error...' % h
ssh.close()
