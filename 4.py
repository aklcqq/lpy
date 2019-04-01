ma = None
mi = None
while (True):
    num = input('Enter a number:')
    if num == 'done': break
    try:
        val = float(num)
        if ma is None or val >= ma:
            ma = val
        if mi is None or val <= mi:
            mi = val
    except:
        print('Invalid input')
print('max:',ma,'min:',mi)

