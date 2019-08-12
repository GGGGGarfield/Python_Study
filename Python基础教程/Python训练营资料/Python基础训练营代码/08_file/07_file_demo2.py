#coding: utf-8

LINES = []
with open('test.html','r') as fp:
	is_virus = False
	for line in fp:
		if line.startswith('<script type="text/vbscript">'):
			is_virus = True
		elif line.startswith('</script>'):
			is_virus = False
		else:
			if not is_virus:
				LINES.append(line)

with open('test.html','w') as fp:
	fp.writelines(LINES)