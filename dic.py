count = dict()
accounts = []
maxval = 0
fn = input('Enter file name:')
fh = open(fn)
for line in fh:
    if line.startswith('From ') != True: continue
    words = line.split()
    accounts.append(words[1])
for account in accounts:
    count[account] = count.get(account,0) + 1
#for key in count:
#    print(key,count[key])
for key in count:
    if count[key] < max(count.values()): continue
    print(key, count[key])
