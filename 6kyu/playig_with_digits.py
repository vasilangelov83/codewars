def dig_pow(n, p):
    result = 0
    for i in range(len(str(n))):
        result += int(str(n)[i])**(p+i)
    if result % n == 0:
        return result // n
    else: return -1
print(dig_pow(46288, 3))