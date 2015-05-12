import re
import urllib

#http://www.pythonchallenge.com/pc/def/linkedlist.php
#start from 12345
id = '8022'
url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
while True:
	print(id)
	s = urllib.urlopen(url + id).read()
	a = re.findall('and the next nothing is (\d+)', s)
	if len(a) == 0:
		print('OVER')
		break
	id = a[0]
#end of chain is 16044
#start again from 8022
#end of chain is 66831
#peak.html