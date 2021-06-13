name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
di=dict()
srt = list()
for lines in fh:
    if not lines.startswith('From '):
        continue
    words = lines.split()
    time = words[5].split(':')
    dig = time[0]
    #print(time)
    if dig not in di:
        di[dig]=1
    else:
        di[dig]+=1
for k,v in di.items():
    tup = (k,v)
    srt.append(tup)
srt.sort()
for a,b in srt:
    print(a,b)

