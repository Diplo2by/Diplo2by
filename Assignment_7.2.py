# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line.rstrip()
    atpos=line.find('0')
    num=float(line[atpos:atpos+20])
    count+=1
    add=add+num
avg= add/count
print("Average spam confidence:", avg)
print("Done")
