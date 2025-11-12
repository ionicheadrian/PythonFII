def prob1() -> list[int]:

    n=input("Input:")

    prob1_la_patrat = lambda x: x*x

    lista_patrate = [prob1_la_patrat(i) for i in range(n)]

    print("_".join(map(str,lista_patrate)))
    
    
    return lista_patrate

