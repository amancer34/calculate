# coding=gbk
import random
import sys
import argparse 
import math
from fractions import Fraction

#产生四则运算表达式
def ques():
	brackets = ['(','',')']
	operators = ['+','-','*','/']
	#随机产生运算符
	i1 = random.randint(0,2)
	i2 = random.randint(0,3)
	i3 = random.randint(0,3)
	#随机产生四个数
	number1 = random.uniform(0,1)
	number1 = Fraction(number1).limit_denominator(10)
	number2 = random.uniform(0,1)
	number2 = Fraction(number2).limit_denominator(10)
	number3 = random.randint(1,10)
	number4 = random.randint(1,10)
	#随机产生左括号
	left1 = random.randint(0,1)
	left2 = random.randint(0,1)
	left3 = random.randint(0,1)
	#随机产生右括号
	right1 = random.randint(1,2)
	right2 = random.randint(1,2)
	right3 = random.randint(1,2)
	#括号匹配
	if left1 == 0:
		left2 = 1
		left3 = 1
		if right1 == 2:
			right2 = 1
			right3 = 1
		else:
			right2 = 2
			right3 = 1
	else:
		if left2 == 0:
			left3 = 1
			right1 = 1
			if right2 == 2:
				right3 = 1
			else:
				right3 = 2
		else:
			left3 = 0
			right1 = 1
			right2 = 1
			right3 = 2
	ques = brackets[left1] + str(number1) + operators[i1] + brackets[left2] + str(number2)
	ques += brackets[right1] + operators[i2] + brackets[left3] + str(number3) + brackets[right2]
	ques += operators[i3] + str(number4) + brackets[right3]
	ques = str(ques)
	return ques
	
#判断输入的数据是否正确
def result():
	total = 0
	for i in range(20):
		question = ques()
		print(question)
		res = eval(question)
		ans = input("? ")
		if str(res) == str(ans):
			print("答对啦，你真是个天才！")
			total += 1
		else:
			print("再想想吧，答案似乎是%f" %res)
	print("一共答对" + str(total) + "道题，" + "共20道题！")
	
#命令行输入题目数目
def command_input(num):
	data = open('data.txt','w+')
	if num.isdigit():
		for i in range(int(num)):
			question = ques()
			question1 = question + '='
			res = Fraction(eval(question)).limit_denominator(100000)
			print('{:<50}{:<25}'.format(question1,traversal_dist(str(res))))
			print('{:<50}{:<25}'.format(question1,traversal_dist(str(res))),file = data)
	else:
		print("题目数量必须是正整数。")
		
#将分子分母转换为十进制数
def take_decimalism(dicts = {}):
	j= len(dicts)-1
	sum1 = 0
	for i in range(0,len(dicts)):
		if j < 0:
			break
		sum1 = int(dicts[j]) * int(math.pow(10,i)) + sum1
		j = j-1
	return sum1		
	
#遍历结果，将分子、分母存储到两个字典中并约分
def traversal_dist(res):
	d1={}
	d2={}
	count1=0
	count2=0
	flag=0
	sign=0
	for i in res:
		if i=='-':
			sign=i
			continue
		if i=='/':
			flag=1
			continue
		if flag==0:
			d1[count1]=i
			count1=count1+1
		else:
			d2[count2]=i
			count2=count2+1
	#分子
	numerator = take_decimalism(d1)
	#分母
	denominator = take_decimalism(d2)
	if denominator == 0:
		return numerator
	else:
		w1=numerator // denominator
		w2=numerator % denominator
		answer=0
		if sign=='-':
			if w1==0:
				answer=sign+str(w2)+"/"+str(denominator)
			else:
				answer=sign+str(w1)+" " +str(numerator)+"/"+str(denominator)
		else:
			if w1==0:
				answer=str(w2)+"/"+str(denominator)
			else:
				answer=str(w1)+" " +str(numerator)+"/"+str(denominator)
		return answer

if __name__ == "__main__":
	#创建对象
	parser = argparse.ArgumentParser()
	#添加参数-c
	parser.add_argument("-c","--cin")
	#解析添加的参数
	args = parser.parse_args()
	if args.cin == None:
		result()
	else:
		command_input(args.cin)
		
	




