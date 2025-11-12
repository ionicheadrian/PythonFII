def palindrom(x:str):
    litere={}
    for c in x:
        if c in litere:
            litere[c]+=1
        else:
            litere[c]=1
    
    impare=0
    for key in litere:
        if litere[key]% 2 == 1:
            impare +=1
            if impare >=2:
                return False
    return True

x=["salut","capac","test","radar","palindrom"]

for cuv in x:
    print(palindrom(cuv))