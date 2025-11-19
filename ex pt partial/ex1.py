def inversare(s:str) -> str:
    vocale="aeiouAEIOU"
    doar_vocale=[c for c in s if c in vocale]
    rez=[]
    for c in s:
        if c in vocale:
            rez.append(doar_vocale.pop())
        else:
            rez.append(c)
    
    return ''.join(rez)

s="hello Nica"
print(inversare(s))