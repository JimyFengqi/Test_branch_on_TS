#!/usr/bin/python
#coding:utf-8
import os
import sys  


num=[1755,2808,3510,4446,4680,4799,8190,12987,12870,13455]
'''
print "单个组合产品"
for a in range(len(num)):
	for i in (range(1,42000/1755)):

		sum=num[a]*i
		if sum < 42000 and sum > 38240:
			print  "%d * %d = %d" % (num[a],i,sum)
		sum=0
'''
		
print "两个组合产品"	
s=1	
for a in range(len(num)):
	for i in (range(1,42000/1755)):
		for j in range(len(num)):
			for k in (range(1,42000/1755)):
				sum=num[a]*i+ num[j]*k
				if sum < 42000 and sum > 38240:
					print  " %d : %d * %d  + %d *%d= %d" % (s,num[a],i,num[j],k,sum)
					s +=1
				sum=0

'''				
print "三个组合产品"					
for a in range(len(num)):
	for i in (range(1,42000/1755)):
		for j in range(len(num)):
			for k in (range(1,42000/1755)):
				for l in range(len(num)):
					for m in (range(1,42000/1755)):
						sum=num[a]*i+ num[j]*k+num[l]*m
						if sum < 42000 and sum > 38240:
							print  "%d * %d  + %d * %d + %d * %d = %d" % (num[a],i,num[j],k,num[l],m,sum)
						sum=0
		
print "四个组合产品"					
for a in range(len(num)):
	for i in (range(1,42000/1755)):
		for j in range(len(num)):
			for k in (range(1,42000/1755)):
				for l in range(len(num)):
					for m in (range(1,42000/1755)):
						for n in range(len(num)):
							for p in (range(1,42000/1755)):
								sum=num[a]*i+ num[j]*k+num[l]*m+num[n]*p
								if sum < 42000 and sum > 38240:
									print  "%d * %d  + %d * %d + %d * %d + %d * %d= %d" % (num[a],i,num[j],k,num[l],m,num[n],p,sum)
								sum=0		
'''	
'''					
print "五个组合产品"					
for a in range(len(num)):
	for i in (range(1,42000/1755)):
		for j in range(len(num)):
			for k in (range(1,42000/1755)):
				for l in range(len(num)):
					for m in (range(1,42000/1755)):
						for n in range(len(num)):
							for p in (range(1,42000/1755)):
								sum=num[a]*i+ num[j]*k+num[l]*m+num[n]*p
								if sum < 42000 and sum > 38240:
									print  "%d * %d  + %d * %d + %d * %d + %d * %d= %d" % (num[a],i,num[j],k,num[l],m,num[n],p,sum)
								sum=0	
'''						
						
						
						
						
						
						
						
						
						
						
						