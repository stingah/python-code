#this works
def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        return sum(range(b,a+1))
    elif b > a:
        return sum(range(a,b+1))
    else:    
        return a + b


#this is the fastest way possible
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
