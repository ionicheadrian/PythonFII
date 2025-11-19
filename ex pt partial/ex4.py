with open("test.txt", 'r+') as f:  # 'r+' = read + write
    content = f.read()
    print(content)
    linii = content.split('\n')
    print(linii)
    
    f.write("\nsal")  # Scrie la sfârșitul fișierului