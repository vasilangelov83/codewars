import math
def is_square(n):
    if n == 0:
        return True
    if n > 0 and abs(math.sqrt(n)) and abs(math.sqrt(n))**2 == n :
        return True
    else: return False

is_square(0)