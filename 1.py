#http://www.pythonchallenge.com/pc/def/map.html
s = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
ans = []
for val in list(s):
	if val.isalpha():
		ans.append(chr(ord(val) + 2))
	else:
		ans.append(val)
s = ''.join(ans)
print(s)
#map->ocr