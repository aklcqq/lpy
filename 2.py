num = []
while (True):
    val = input('Enter a number:')
    if val == 'done':
        break
    else:
        try:
            val = float(val)
            num.append(val)
        except:
            print('invalid input')
print('max:',max(num),'\nmin',min(num))
