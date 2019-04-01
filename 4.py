num = 0
max = 0
min = 0
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
        max = val
        min = val
        if val > max:
            max = val
        if val < min:
            min = val
    except:
        print('Invalid input')

print('max',max,'min',min)
