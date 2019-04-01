num = 0
count = 0
total = 0
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
        count = count + 1
        total = val + total
        average = total / count

    except:
        print('Invalid input')

print('average',average,'count',count,'sum',total)
