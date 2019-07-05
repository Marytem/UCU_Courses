import math

num = eval(input())
sqrtnum = math.sqrt(num)
halfnum = num/2
accuraсy = int(input()) 

for i in range (accuraсy):
	halfnum = 0.5 * (halfnum + num/halfnum)
	
if num>0:	
	print('number:', num)	
	print('square root:', halfnum)
	print('accuraсy:', accuraсy)
	print('accuraсy difference:', halfnum - sqrtnum)
else: 
	print('error: num<0')	