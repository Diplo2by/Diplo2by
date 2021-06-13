import re
f = open('regex.txt')
li = list()
for lines in f:
    num = re.findall('[0-9]+',lines)
    if len(num) > 0:
        for i in num:
            li.append(int(i))
print(sum(li))
