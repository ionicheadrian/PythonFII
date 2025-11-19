# se da ca input un string de numere, sa se faca media numerelor pozitive din sir
# se va verifica daca sirul contine cel putin un numar pozitiv real, altfel se semnaleaza acest lucru
# se va verifica daca inputul are DOAR numere si spatii (74 20.2 3.1 50)

def numere(s: str)-> float:
    nr=s.split()
    s=0
    k=0
    for elem in nr:
        try:
            n=float(elem)
        except ValueError:
            return "invalid data"
        
        if n>0:
            s+=n
            k+=1
    
    if k==0:
        return "Nu exista numere pozitive :("

    return s / k 


input=input("introdu numere: ")
print("="*10)
print(numere(input))