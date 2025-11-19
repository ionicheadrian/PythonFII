def analyze_scores(scores: list[tuple[str,int]]) -> dict:
    avg=0
    unique_scores= set()
    maxi=-1
    rez={}
    for name,score in scores:
        avg+=score
        unique_scores.add(score)
        if score > maxi:
            maxi= score
            top_scorer = name

    avg=avg/len(scores)
    rez ={
        "average" : avg,
        "unique_scores" : sorted(unique_scores),
        "top_scorer" : top_scorer
    }
    
    return rez

input_data = [('Alice', 90), ('Bob', 80), ('Michael', 95), ('Gabe', 80)]
print(input_data)
print(analyze_scores(input_data))

input_data = [('Ana', 100), ('Ion', 85), ('Maria', 92), ('Paul', 100)]
print(input_data)
print(analyze_scores(input_data))

input_data = [('Elena', 70), ('George', 75), ('Radu', 60), ('Diana', 85)]
print(input_data)
print(analyze_scores(input_data))

input_data = [('Alex', 88), ('Bianca', 88), ('Cristi', 91), ('Daria', 95)]
print(input_data)
print(analyze_scores(input_data))