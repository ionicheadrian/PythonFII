def comparareseturi(*seturi):
    rez={}
    
    for i in range(len(seturi)):
        for j in range(len(seturi)):
            if i!=j:
                a=seturi[i]
                b=seturi[j]

                #REUNIUNE
                c=set()
                for elem in a:
                    c.add(elem)
                for elem in b:
                    c.add(elem)
                
                cheie=f"{a} | {b}"
                rez[cheie]=c
                
                #INTERSECTIE
                c=set()
                for elem in a:
                    if elem in b:
                        c.add(elem)
                
                cheie=""
                cheie=f"{a} & {b}"
                rez[cheie]=c

                #Diferenta
                c=set()
                for elem in a:
                    if elem not in b:
                        c.add(elem)

                cheie=""
                cheie=f"{a} - {b}"
                rez[cheie]=c
    
    return rez


rez = comparareseturi({1, 2}, {2, 3})
for key, value in rez.items():
    print(f"{key}: {value}")
