try:
    num = input('Enter a number:')
    num = float(num)
    max = num
    min = num
except:
    print('Invalid input')
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
        if val >= max:
            max = val
        if val <= min:
            min = val



    except:
        print('Invalid input')
print('max',max,'min',min)
