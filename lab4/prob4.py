def loop(mapping):
    vizitat = set()
    rez = []
    c = "start"

    while c in mapping:
        val = mapping[c]

        if c in vizitat:
            break
        
        rez.append(val)
        vizitat.add(c)
        
        c = mapping[c]
    
    return rez


print("Test 1")
test1 = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(test1)
print(loop(test1))

print("Test 2")
test2 = {'start': 'x', 'x': 'y', 'y': 'x', 'z': 'w'}
print(test2)
print(loop(test2))

print("Test 3")
test3 = {'start': 'a', 'a': 'b', 'b': 'c', 'c': 'start'}
print(test3)
print(loop(test3))