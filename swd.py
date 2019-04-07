import re
fn = input('Enter file:')
fh = open(fn)
swrd = input('Enter a regular expression:')
count = 0
sumall = 0
p = []
for line in fh:
    line = line.rstrip()
    x = re.findall(swrd,line)
    if len(x) > 0:
        count = count + 1
        for num in x:
            num = int(num)
        sumall = sumall + num
cal = input('Compute the average? y/n')
if cal == 'y':
    print(sumall / count)
else:
    exit()
p = 'New.*: ([0-9]+)'
