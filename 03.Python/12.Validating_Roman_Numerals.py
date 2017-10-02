# CDXXI

# From : http://www.diveintopython3.net/regular-expressions.html
# Sometimes , I feel so stupid.


from roman import fromroman

try:
    if 0<fromRoman(input())<4000:
        print(True)
    else:
        print(False)
except:
    print(False)

# import re

# s = input()
# isRomanNumeral = True
# patern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
# m = re.search(r'%s' % patern, s)
# print (bool(m))
        
