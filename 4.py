num = 0
max = num
min = num
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
