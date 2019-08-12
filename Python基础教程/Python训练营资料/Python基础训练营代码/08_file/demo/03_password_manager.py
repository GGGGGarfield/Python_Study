
import getpass
import hashlib
from functools import reduce

FILE_NAME = 'password_book.txt'
PASSWORD = None

def ord_password():
	# 1. 首先要对这个密码中所有的字符求ascii对应的码
	# 2. 把这个密码中所有的字符的ascii码相加
	return reduce(lambda x,y:x+y,map(lambda x:ord(x),PASSWORD))

def list_all_password():
	with open(FILE_NAME,'r') as fp:
		index = 0
		print('='*30)
		for line in fp:
			index += 1
			if index == 1:
				continue
			# 393_409_394_404:416_398_399_402_399_391_405:343_343_343_343_343_343
			# 1. 根据:进行分割，第一个部分表示的是产品，第二部分表示的是用户名，第三部分表示的是密码
			infos = line.split(':')
			# 2. 对每个部分进行分割按照_进行分割，每个下划线旁边的值就是一个字符的ascii值
			# 产品解密
			# 3. 对每一个ascii值进行chr操作，就是把ascii值转换为具体的字符
			product_ord = infos[0]
			product_ord_list = product_ord.split('_')
			product = ''.join(map(lambda x:chr(int(x)-ord_password()),product_ord_list))

			# 用户名解密
			username_ord = infos[1]
			username_ord_list = username_ord.split('_')
			username = ''.join(map(lambda x:chr(int(x)-ord_password()),username_ord_list))

			# 密码解密
			password_ord = infos[2]
			password_ord_list = password_ord.split('_')
			password = ''.join(map(lambda x:chr(int(x)-ord_password()),password_ord_list))
			
			print('产品：%s，用户名：%s，密码：%s' % (product,username,password))

		print('='*30)

def add_password():
	# 1. 产品名字
	product = input('请输入产品名称：')
	# 2. 用户名
	username = input('请输入用户名：')
	# 3. 密码
	password = input('请输入密码：')
	# ord函数：是将英文字母或者阿拉伯数字或者英文标点符号转换为ascii码
	# 'csdn'  => '100_120_98_130'
	ord_pwd = ord_password()
	hashed_product = '_'.join(list(map(lambda x:str(ord(x)+ord_pwd),product)))
	hashed_name = '_'.join(list(map(lambda x:str(ord(x)+ord_pwd),username)))
	hashed_password = '_'.join(list(map(lambda x:str(ord(x)+ord_pwd),password)))
	# product_list = [99, 115, 100, 110] = [99+294,115+294,100+249,110+249] = []
	# '111111' => [49,49,49,49,49,49] = 294
	# 'xx_xx_xx:yy_zz'
	line = "{product}:{username}:{password}".format(product=hashed_product,username=hashed_name,password=hashed_password)
	with open(FILE_NAME,'a') as fp:
		fp.write(line+'\n')

	print('恭喜！密码存储成功！')

def index_page():
	print("===欢迎进入密码管理系统===")
	print("0. 退出系统")
	print("1. 添加新密码")
	print("2. 查看所有密码")
	while True:
		value = input('请输入您要做的操作：')
		if value == '0':
			# 跳出当前系统
			break
		elif value == '1':
			# 添加新密码
			add_password()
		elif value == '2':
			# 查看所有密码
			list_all_password()
		else:
			print('您输入的操作有误，请重新输入！')


def login_page():
	with open(FILE_NAME,'r') as fp:
		while True:
			pwd = getpass.getpass('[登录]请输入登录密码：')
			hashed_pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
			line = fp.readline().replace('\n','')
			if line == hashed_pwd:
				# 认为是登录成功
				# 跳转到主页
				global PASSWORD
				PASSWORD = pwd
				index_page()
			else:
				# 密码错误
				print('密码错误，请重新输入！')
				continue


def is_first_use():
	first = False
	try:
		with open(FILE_NAME,'r') as fp:
			line = fp.readline()
			if line:
				first = False
			else:
				first = True
	except FileNotFoundError:
		first = True

	return first

def main():
	print('===密码管理系统===')
	# 1. 要判断这个用户是否第一次使用这个系统，如果是第一次使用这个系统
	# 那么应该先要让用户初始化一下系统的密码
	if is_first_use():
		# 让用户取初始化密码
		while True:
			pw1 = getpass.getpass('[初始化]请输入系统管理密码：')
			pw2 = getpass.getpass('[初始化]请确认系统管理密码：')
			if pw1 != pw2:
				print('两次密码不一致，请重新输入！')
			else:
				# 如果两次密码是一致的，说明用户输入的密码是正确的
				# 1. 要把用户输入的密码加密后存储到文件中
				hashed_pwd = hashlib.md5(pw1.encode('utf-8')).hexdigest()
				with open(FILE_NAME,'w') as fp:
					fp.write(hashed_pwd+'\n')
				# 2. 跳转到登录页面

				# 3. break
				break

	else:
		# 让用户去做登录的操作
		# 2. 使用getpass模块下的getpass函数来接收用户输入的密码
		# getpass这个函数可以在用户输入密码的时候，把密码隐藏，因此更加安全
		# 不要使用input函数
		# password = getpass.getpass('请输入系统管理密码：')
		login_page()


if __name__ == '__main__':
	main()