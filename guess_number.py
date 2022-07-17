#隨機產生數字當答案，讓user猜數字
#猜錯的話 提示大小

import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字 : ')
	num = int(num)
	if num == r:
		print('答對了!')
		break
	else:
		if num < r:
			print('比', num, '大')
		else:
			print('比', num, '小')