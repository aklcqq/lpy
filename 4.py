try:
    num = input('Enter a number:')
    num = float(num)
    ma = num
    mi = num
except:
    print('Invalid input')
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
        if val >= ma:
            ma = val
        if val <= mi:
            mi = val



    except:
        print('Invalid input')
print('ma',ma,'mi',mi)

