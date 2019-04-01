num = 0
count = 0
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
    except:
        print('Invalid input')
    total = val + total
    count = count + 1
average = total / count
print('average',average,'count',count,'sum',total)
