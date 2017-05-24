#!/usr/bin/env python
import os,sys
import psutil
import commands

def Server(kube_pid):
  pid=int(kube_pid)
  if psutil.Process(pid).name():
    print "process is running..."


if __name__=='__main__':
  kube_name=['kube-proxy','kube-controller-manager','kube-scheduler','kubelet']
  for i in kube_name:
    try:
      cmd='ps aux|grep %s|grep -v "grep"' % i
      kube_pid=commands.getoutput(cmd).split()[1]
      Server(kube_pid)
    except IndexError,e:
      os.system('systemctl restart %s ' % i)

