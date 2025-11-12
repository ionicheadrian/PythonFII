def extract_nr(s:str):
    cuvinte=s.split()
    for cuv in cuvinte:
        if cuv.isnumeric()==1:
            return cuv
            break
        
s="am 10 lei in buzunar"
print(extract_nr(s)) #expected 10
s="am 20 lei in buzunar, dar 740000 in V-Bucks :D"
print(extract_nr(s)) #expected 20 (trb prima valoare)
