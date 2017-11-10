#!/usr/bin/python
#coding:utf-8
import os
import sys  


num=[1755,2808,3510,4446,4680,4799,8190,12987,12870,13455]

print "单个组合产品"

total_list=[]

for a in range(len(num)):
	for i in (range(1,40001/1755)):
		tmp_data={} #临时变量-
		print_sen=''#临时变量--存贮打印语句
		
		sum=num[a]*i
		if sum < 40001 and sum > 38000:
			print  "%d * %d = %d" % (num[a],i,sum)
			print_sen="%d * %d = %d" % (num[a],i,sum)#组装打印输出语句

			
			tmp_data['sum_num']=sum                #将数值与打印语句绑定在一起
			tmp_data['print_sen']=print_sen		   
			total_list.append(tmp_data)
		sum=0#重置数据

print "两个组合产品"		
for a in range(len(num)):
	for i in (range(1,40001/1755)):
		for j in range(len(num)):
			for k in (range(1,40001/1755)):
				tmp_data={} #临时变量-
				print_sen=''#临时变量--存贮打印语句
				
				sum=num[a]*i+ num[j]*k
				if sum < 40001 and sum > 38000:
					print  "%d * %d  + %d *%d= %d" % (num[a],i,num[j],k,sum)
					print_sen="%d * %d  + %d *%d= %d" % (num[a],i,num[j],k,sum)#组装打印输出语句
					
					tmp_data['sum_num']=sum                #将数值与打印语句绑定在一起
					tmp_data['print_sen']=print_sen		   
					
					total_list.append(tmp_data)				#将数据加入总的list里面
				sum=0 #
		


	
		
print "三个组合产品"					
for a in range(len(num)):
	for i in (range(1,40001/1755)):
		for j in range(len(num)):
			for k in (range(1,40001/1755)):
				for l in range(len(num)):
					for m in (range(1,40001/1755)):
						tmp_data={} #临时变量-
						print_sen=''#临时变量--存贮打印语句
						sum=num[a]*i+ num[j]*k+num[l]*m
						if sum < 40001 and sum > 38000:
							print  "%d * %d  + %d * %d + %d * %d = %d" % (num[a],i,num[j],k,num[l],m,sum)
							print_sen = "%d * %d  + %d * %d + %d * %d = %d" % (num[a],i,num[j],k,num[l],m,sum)
							
							tmp_data['sum_num']=sum                #将数值与打印语句绑定在一起
							tmp_data['print_sen']=print_sen		   
							total_list.append(tmp_data)				#将数据加入总的list里面
						sum=0
		
print "四个组合产品"					
for a in range(len(num)):
	for i in (range(1,40001/1755)):
		for j in range(len(num)):
			for k in (range(1,40001/1755)):
				for l in range(len(num)):
					for m in (range(1,40001/1755)):
						for n in range(len(num)):
							for p in (range(1,40001/1755)):
								tmp_data={} #临时变量-
								print_sen=''#临时变量--存贮打印语句
								
								
								sum=num[a]*i+ num[j]*k+num[l]*m+num[n]*p
								if sum < 40001 and sum > 38000:
									print  "%d * %d  + %d * %d + %d * %d + %d * %d= %d" % (num[a],i,num[j],k,num[l],m,num[n],p,sum)
									print_sen = "%d * %d  + %d * %d + %d * %d + %d * %d= %d" % (num[a],i,num[j],k,num[l],m,num[n],p,sum)
									
									tmp_data['sum_num']=sum                #将数值与打印语句绑定在一起
									tmp_data['print_sen']=print_sen		   
					
									total_list.append(tmp_data)				#将数据加入总的list里面
								sum=0		

								
'''					
print "五个组合产品"					
for a in range(len(num)):
	for i in (range(1,40001/1755)):
		for j in range(len(num)):
			for k in (range(1,40001/1755)):
				for l in range(len(num)):
					for m in (range(1,40001/1755)):
						for n in range(len(num)):
							for p in (range(1,40001/1755)):
								sum=num[a]*i+ num[j]*k+num[l]*m+num[n]*p
								if sum < 40001 and sum > 38000:
									print  "%d * %d  + %d * %d + %d * %d + %d * %d= %d" % (num[a],i,num[j],k,num[l],m,num[n],p,sum)
								sum=0	
'''						
						
	
	
	
#排序并输出最后结果
total_list = sorted(total_list,cmp=lambda x,y:cmp(x['sum_num'],y['sum_num']),reverse=0)		

print "排序之后输出结果："	
print len(total_list)
for a in total_list:
	print a['print_sen']				
						
						
						
						
						
						
						