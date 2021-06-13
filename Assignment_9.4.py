name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
senders=dict()
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    mail = words[1]
    if mail not in senders:
        senders[mail] = 1
    else:
        senders[mail] +=1
bigword = None
bigcount = None
for a,b in senders.items():
    if bigcount is None or bigcount < b:
        bigcount = b
        bigword= a

print(bigword, bigcount)
#print(senders)

     