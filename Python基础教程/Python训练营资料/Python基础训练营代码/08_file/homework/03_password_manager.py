#coding: utf-8
import hashlib
import getpass
from functools import reduce

PASSWORD_FILE_NAME = 'password_book.txt'
PASSWORD = None

def login_check():
	"""
	登录检查的
	"""
	def check_password(pwd):
		"""
		检查用户输入的密码是否正确！
		"""
		with open(PASSWORD_FILE_NAME,'r') as fp:
			hashed_pwd = fp.readline().replace('\n','')
			# md5('abc') = 'aaaaaasdf'
			# md5('abc') = 'aaaaaasdf'
			if hashlib.md5(bytes(pwd,encoding='utf-8')).hexdigest() == hashed_pwd:
				# 如果密码验证正确，记录这个密码
				global PASSWORD
				PASSWORD = pwd
				return True
			else:
				return False

	while True:
		pwd = getpass.getpass(u'请输入登录密码：')
		if check_password(pwd):
			return True
		else:
			# 如果密码错误，重新输入
			print(u'密码错误，请重新输入！')


def init_password():
	"""
	第一次使用这个系统，初始化密码！
	"""
	init_pwd = None
	while True:
		pwd1 = getpass.getpass(u"请输入初始化密码（没有找回密码功能）：")
		pwd2 = getpass.getpass(u"请确认密码（没有找回密码功能）：")
		if pwd1 != pwd2:
			print(u'两次密码不一致，请重新输入！')
		else:
			init_pwd = pwd1
			break

	# md5加密后，存储到文件的第一行
	with open(PASSWORD_FILE_NAME,'w') as fp:
		hashed_pwd = hashlib.md5(bytes(init_pwd,encoding='utf-8')).hexdigest()
		fp.write(hashed_pwd+'\n')

	print(u'恭喜！初始密码设置完毕！')


def is_first_use():
	"""
	是否是第一次使用
	"""
	try:
		with open(PASSWORD_FILE_NAME,'r') as fp:
			line = fp.readline()
			if not line:
				return True
			else:
				return False
	except:
		return True

def ord_password():
	"""
	将密码中所有的字符全部转换为ascii码对应的值，并且求他们的和
	"""
	if not PASSWORD:
		return None
	return reduce(lambda x,y:int(x)+int(y),map(lambda x:ord(x),PASSWORD))

def add_password():
	"""
	用来存储密码
	"""
	product = input(u'请输入产品名称：')
	username = input(u'请输入用户名：')
	password = input(u'请输入密码：')

	ord_pwd = ord_password()

	product_hashed = '_'.join(map(lambda x:str(ord(x)+ord_pwd),product))
	username_hashed = '_'.join(map(lambda x:str(ord(x)+ord_pwd),username))
	password_hashed = '_'.join(map(lambda x:str(ord(x)+ord_pwd),password))
	
	with open(PASSWORD_FILE_NAME,'a') as fp:
		fp.write('%s:%s:%s\n'%(product_hashed,username_hashed,password_hashed))
	print('恭喜！密码存储成功！')

def list_all_password():
	"""
	列出所有的密码
	"""
	with open(PASSWORD_FILE_NAME,'r') as fp:
		index = 0
		for line in fp:
			if index == 0:
				index += 1
				continue
			product_hashed,username_hashed,password_hashed = line.split(':')
			
			product_hashed_list = product_hashed.split('_')
			product = ''.join(map(lambda x:chr(int(x)-ord_password()),product_hashed_list))

			username_hashed_list = username_hashed.split('_')
			username = ''.join(map(lambda x:chr(int(x)-ord_password()),username_hashed_list))

			password_hashed_list = password_hashed.replace('\n','').split('_')
			password = ''.join(map(lambda x:chr(int(x)-ord_password()),password_hashed_list))

			print('产品：%s，用户名：%s，密码：%s' % (product,username,password))

def index_page():
	if not PASSWORD:
		return
	print('0. 退出当前系统')
	print('1. 增加密码')
	print('2. 查看所有密码')
	while True:
		option = input(u'请输入选项：')
		if option == '1':
			# 做增加密码的功能
			add_password()
		elif option == '2':
			# 做查看所有密码的功能
			list_all_password()
		elif option == '0':
			break
		else:
			print(u'您输入的选项不对，请重新输入！')

def main():
	"""
	主函数，用来控制流程的
	"""
	print(u'===密码管理系统===')
	# 如果是第一次使用
	if is_first_use():
		# 调用初始化密码操作
		init_password()

	if login_check():
		# 如果登录验证通过，则进入到主界面
		index_page()


if __name__ == '__main__':
	main()