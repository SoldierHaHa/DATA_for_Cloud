import re
s = input("请输入用户名：")
reg = r'''[A-Z][a-z]{6}\d{2}'''
regex = re.compile(reg)
m = re.match(regex,s)
if m:
    print("输入正确")
else:
    print("输入错误")
