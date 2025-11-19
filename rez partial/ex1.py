#sa scriem un program care sa numere toate cifrele (0-9) dintr un sir

def nr_count(s: str)->int:
    k=0
    for c in s:
        if c.isnumeric()==1:
            k+=1
    return k

s="test123"
print(nr_count(s)) #expected 3