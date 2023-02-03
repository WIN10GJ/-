import itertools as its
import datetime

# 记录程序运行时间
start = datetime.datetime.now()
words = '0123456789'# 大小写字母 + 数字 + 符号 组合
# words = '0123456789' # 纯数字
# 生成密码的位数
r = its.product(words, repeat=6)  # 即生成6位密码，正常情况下密码位数为6
dic = open(r"D:\新建文件夹 (3)\OneDrive\桌面\新建文本文档.txt", 'a')  # alphabetPass.txt 是密码本名称
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
    print(i)

dic.close()
print('密码本生成好了')
end = datetime.datetime.now()
print("生成密码本一共用了多长时间：{}".format(end - start))