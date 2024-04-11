drive = input('請問你有沒有開過車?')
if drive != '有' and drive != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit #終止程式

age = input('請問你的年齡?')
age = int(age) #要轉換成整數，才能做比較!!
if drive == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('未通過')
elif drive == '沒有':
	if age >= 18:
		print('快去考駕照')
	else:
		print('正常的，再等等吧')

else:
	print('只能輸入有或沒有')
