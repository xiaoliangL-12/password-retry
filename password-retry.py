"*练习, 密码重试程序"
#设定好password=a123456, 最多输入3次密码
#密码不对的话印出"密码错误"以及还有几次机会
#对的话就登出"登入成功!"

password = 'a123456'
i = 3                                 #剩余机会
while True:
	pwd = input('请输入密码: ')
	if pwd == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('密码错误! 还有', i, '次机会')
		if i == 0:
			print('密码错误, 账号已冻结')
			break







