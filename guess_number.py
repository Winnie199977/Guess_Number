#隨機產生數字當答案，讓user猜數字
#猜錯的話 提示大小

import random

r = random.randint(1, 100)
count = 0

while True:
	count += 1
	num = input('請猜數字 : ')
	num = int(num)
	if num == r:
		print('答對了!')
		print('總共猜了', count, '次')
		break
	elif num < r:
		print('比', num, '大')
	elif num > r:	
		print('比', num, '小')			
	print('已經猜了', count, '次')