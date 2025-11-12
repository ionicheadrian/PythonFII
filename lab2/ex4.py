def to_binary(x:int):
    res=0
    power=1
    while x :
        res = res + (x%2) * power
        power *=10
        x//=2

    return res

print(to_binary(50))