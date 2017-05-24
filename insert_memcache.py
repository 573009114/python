#!/usr/bin/env python
#coding:utf-8
from pymemcache.client.hash import HashClient 
from pymemcache.client.base import Client
import sys,os,time

class memcache:

	def __init__(self,ip='10.20.28.228',key='dbkey',value='new_value'):
		self.ip=ip
		self.key=key
		self.value=value
		#self.client = HashClient([(self.ip, 30212),(self.ip,30213)])
		self.client= Client((self.ip,30001))
		while True:
			try:
				self.num=int(raw_input('需要多少个ID ?  '))
				break
			except ValueError:
				print "输入错误"
	
	def insert(self):
		for i in range(1,self.num):
			key=self.key+str(i)
			value=self.value+str(i)
			try:
				if self.client.get(key):
					print key ,'value is exist'
				else:
					self.client.set(key,value) 
					print key , 'insert success...'
			except Exception:
				print "MemcacheServerError"


	def view(self):
		try:
			start_num=int(raw_input('输入查看的起始ID,默认为1: '))
			if start_num:
 				s_num=start_num
		except ValueError:
			s_num=int(1)

		for j in range(s_num,self.num):
			key=self.key+str(j)
			try:
				result=self.client.get(key)
				if (result == None):
					print key,'is null'
				else:
					print result
			except Exception:
				print Exception
			
if __name__ == '__main__':
	in_put=raw_input('[按[k]插入Key | 按[v]查看Value]:\n ')
	if in_put == 'k':
		memcache().insert()
	elif in_put == 'v':
		memcache().view()
	else:
		print "程序退出... 用法错误，输入k插入，输入v查看 "
