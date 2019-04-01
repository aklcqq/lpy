## Use find and string slicing to extract the portion of the string after the
## colon character and then use the float function to convert the extracted
## string into a floating point number.


#loccolon = None
str = 'X-DSPAM-Confidence:0.8475'
#loccolon = int(str.find(':')) + 1
#loccolon = int(loccolon) + 1
print(float(str[int(str.find(':')) + 1:]))
#str = float(str)
#print(str)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('Error: Cannot open file')
    exit()

#for i in fhand:
#    i = i.upper()
#    print(i)

count = 0
tar = 0
srchwrd = input('Search word:')
for b in fhand:
    l = b.rstrip()
    if srchwrd in l:
        count = count + 1
        tar = float(str[int(l.find(':')) + 1:]) + tar
        print(l)
print('count:',count,'avg:',tar / count)
