#!/usr/bin/python
#coding:utf-8
import os
from itertools import combinations



price_single_list=[1755,2808,3510,4446,4680,4799,8190,12987,12870,13455]
price_final_range=[38000,40000]

print "单个组合产品"


#传入参数 num:  指定的数组
#传入参数 n:   将要从数组中挑选的个数
#返回不重复的排列组合列表
def get_combination(price_single_list,n):
	price_combination_lists= [c for c in combinations(price_single_list,n)]
	return price_combination_lists

	
#只选择一种产品组合成的报价	
def get_1_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in (range(40000/13455,40000/1755+1)):
			sum_price=single_list[0]*a1
			print "%d * %d  = %d" % ( single_list[0],a1,sum_price)
			if sum_price< 40000 and sum_price > 38000:
				print "第%d种  %d * %d  = %d" % (i,single_list[0],a1,sum_price)
				i +=1	

#只选择2种产品组合成的报价
def get_2_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in range(40000/13455,40000/1755+1):
			for a2 in range(40000/13455,40000/1755+1):
				sum_price=single_list[0]*a1+single_list[1]*a2
				if sum_price< 40000 and sum_price > 38000:
					print "第%d种  %d * %d + %d * %d  = %d" % (i,single_list[0],a1,single_list[1],a2,sum_price)
					i +=1
					
#只选择3种产品组合成的报价
def get_3_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in range(1,40000/1755+1):
			for a2 in range(1,40000/1755+1):
				for a3 in range(1,40000/1755+1):
					sum_price=single_list[0]*a1+single_list[1]*a2+single_list[2]*a3
					if sum_price< 40000 and sum_price > 38000:
						print "第%d种  %d * %d + %d * %d+ %d * %d   = %d" % (i,single_list[0],a1,single_list[1],a2,single_list[2],a3,sum_price)
						i +=1	
#只选择4种产品组合成的报价
def get_4_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in range(1,40000/1755+1):
			for a2 in range(1,40000/1755+1):
				for a3 in range(1,40000/1755+1):
					for a4 in range(1,40000/1755+1):
						sum_price=single_list[0]*a1+single_list[1]*a2+single_list[2]*a3+single_list[3]*a4
						if sum_price< 40000 and sum_price > 38000:
							print "第%d种  %d * %d + %d * %d+ %d * %d + %d * %d = %d" % (i,single_list[0],a1,single_list[1],a2,single_list[2],a3,single_list[3],a4,sum_price)
							i +=1							

#只选择5种产品组合成的报价
def get_5_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in range(1,40000/1755+1):
			for a2 in range(1,40000/1755+1):
				for a3 in range(1,40000/1755+1):
					for a4 in range(1,40000/1755+1):
						for a5 in range(1,40000/1755+1):
							sum_price=single_list[0]*a1+single_list[1]*a2+single_list[2]*a3+single_list[3]*a4+single_list[4]*a5
							if sum_price< 40000 and sum_price > 38000:
								print "第%d种  %d * %d + %d * %d+ %d * %d + %d * %d +%d * %d = %d" % (i,single_list[0],a1,single_list[1],a2,single_list[2],a3,single_list[3],a4,single_list[4],a5,sum_price)
								i +=1	


#只选择4种产品组合成的报价
def get_6_result(price_combination_lists):
	i=1
	for single_list in price_combination_lists:
		for a1 in range(1,40000/1755+1):
			for a2 in range(1,40000/1755+1):
				for a3 in range(1,40000/1755+1):
					for a4 in range(1,40000/1755+1):
						for a5 in range(1,40000/1755+1):
							for a6 in range(1,40000/1755+1):
								sum_price=single_list[0]*a1+single_list[1]*a2+single_list[2]*a3+single_list[3]*a4+single_list[4]*a5+single_list[5]*a6
								if sum_price< 40000 and sum_price > 38000:
									print "第%d种  %d * %d + %d * %d+ %d * %d + %d * %d +%d * %d +%d * %d = %d" % (i,single_list[0],a1,single_list[1],a2,single_list[2],a3,single_list[3],a4,single_list[4],a5,single_list[5],a6,sum_price)
									i +=1	

								
price_combination_lists=get_combination(price_single_list,6)
get_6_result(price_combination_lists)
	
'''

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
					
						
	
	
	
#排序并输出最后结果
total_list = sorted(total_list,cmp=lambda x,y:cmp(x['sum_num'],y['sum_num']),reverse=0)		

print "排序之后输出结果："	
print len(total_list)
for a in total_list:
	print a['print_sen']				
						
						
						
	'''					
						
						
						
