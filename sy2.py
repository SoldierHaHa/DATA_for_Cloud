import re
s = input("请输入：")
reg = r'''\d+'''
regex = re.compile(reg)
nlist = re.findall(regex,s)
n=""
for d in nlist:
    n += d
print(n)
