def comparamdict(dict1, dict2):
    # comparam 2 dictionare recursiv 
    
    #verificam daca sunt de acelasi tip
    if type(dict1) != type(dict2):
        return False
    
    #verif daca sunt dictionare
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        # verfic daca au aceleasi chei
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        
        # acum verf daca toate valorile
        for key in dict1:
            if not comparamdict(dict1[key], dict2[key]):
                return False
        return True 
    
    
    if isinstance(dict1, (list, tuple)) and isinstance(dict2, (list, tuple)):
        if len(dict1) != len(dict2):
            return False
        
        for i, j in zip(dict1, dict2):
            if not comparamdict(i, j):
                return False
        return True 
    
    
    return dict1 == dict2


print("Test 1")
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}
dict3 = {'a': 1, 'b': 3}
print(f"dict1 == dict2: {comparamdict(dict1, dict2)}") 
print(f"dict1 == dict3: {comparamdict(dict1, dict3)}")  

print("Test 2")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(f"list1 == list2: {comparamdict(list1, list2)}") 
print(f"list1 == list3: {comparamdict(list1, list3)}")

print("TEst 3")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)
print(f"tuple1 == tuple2: {comparamdict(tuple1, tuple2)}")
print(f"tuple1 == tuple3: {comparamdict(tuple1, tuple3)}")

print("Test 4")
list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
print(f"list == tuple: {comparamdict(list1, tuple1)}")

print("Test 5")
dict1 = {'a': 1, 'b': [2, 3, 4]}
dict2 = {'a': 1, 'b': [2, 3, 4]}
dict3 = {'a': 1, 'b': [2, 3, 5]}
print(f"dict1 == dict2: {comparamdict(dict1, dict2)}")
print(f"dict1 == dict3: {comparamdict(dict1, dict3)}")

print("Test 6")
list1 = [1, {'x': 10, 'y': 20}, 3]
list2 = [1, {'x': 10, 'y': 20}, 3]
list3 = [1, {'x': 10, 'y': 99}, 3]
print(f"list1 == list2: {comparamdict(list1, list2)}")
print(f"list1 == list3: {comparamdict(list1, list3)}")

print("Test 7")
complex1 = {
    'name': 'Ana',
    'scores': [10, 20, 30],
    'info': {
        'age': 25,
        'courses': ('Math', 'CS')
    }
}
complex2 = {
    'name': 'Maria',
    'scores': [10, 74, 30],
    'info': {
        'age': 22,
        'courses': ('Python', 'CS')
    }
}
complex3 = {
    'name': 'Ana',
    'scores': [10, 20, 30],
    'info': {
        'age': 25,
        'courses': ('Math', 'CS')
    }
}