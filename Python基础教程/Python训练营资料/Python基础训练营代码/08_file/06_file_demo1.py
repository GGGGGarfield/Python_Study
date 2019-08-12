#coding: utf-8

# a => [] => b
# a => b

# lines = []
# with open('xxx.txt','r') as fp:
# 	for line in fp:
# 		lines.append(line)


# with open('xxx[copy].txt','w') as fp:
# 	fp.writelines(lines)

with open('xxx.txt','r') as fp1:
	with open('xxx[copy].txt','w') as fp2:
		for line in fp1:
			fp2.write(line)
