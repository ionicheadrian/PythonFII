def coutingchars(text):
    #numaram fiecare caracter dintr-un sir de caractere si le contorizam intr-un dictionar
    dict={}
    for char in text:
        if char != ' ':
            if char in dict:
                dict[char]=dict[char]+1
            else:
                dict[char]=1
    return dict

enunt="aabbbcccc..!"
print(coutingchars(enunt))