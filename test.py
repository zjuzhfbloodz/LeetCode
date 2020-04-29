import math
def get_factors(n):
    out = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            out.append(i)
    return out

#print(get_factors(6386016))
print(6386016/301)
