
def Converter(list):
    list_bool = {}
    
    for item in list:
        if item == "Even":
            list_bool["Even"] = True
            continue
        if item == "Odd":
            list_bool["Even"] = False
            continue
            
        if item.startswith("Not "):
            key= item[4:]
            list_bool[key] = False
        else:
            list_bool[item] = True
            
    return list_bool

def Pair_Generator(dict):
    pairs= []
    keys= list(dict.keys())
    
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            pairs.append((keys[i], keys[j]))
            
    return pairs

def get_pair_score(min, max, score):
    shifted= score-min
    diff= max-min
    result= round((shifted/diff), 2) * 10
    return result


def Sanity_Check(subject, baseline):
    benchmark= 0
    for item in baseline:
        if item in subject:
            Error= None
            continue
        else:
            print(f"Error In Math List.\n {item} is not in Subject(Main) List.")
            Error= True
            break
    if Error:
        benchmark -= 10
    else:
        benchmark += 10
            
    return benchmark
    
def Difficulty_Check(subject, baseline):
    benchmark= 0
    match= 0
    items= 0
    ideal= 40
    for key in baseline:
        items += 1
        if key in subject:
            match += 1
        
    match_mark= round((match/items), 3) * 100
    difference= abs(match_mark - ideal)
    score= 100 - difference
    benchmark= score/10
    
    return benchmark
    

def Pair_Check(subject):
    benchmark= 0
    pairs= []
    
    pairs= Pair_Generator(dict=subject)
    
    #print(pairs)
    
    for a, b in pairs:
        score= 0
        impact= 0
        val_a= subject[a]
        val_b= subject[b]
        
        #print(val_a, val_b)
        
        if a == "Even" and b == "Prime":
            impact= 3
            if val_a and val_b:
                score= -2 * impact
            elif val_a != val_b:
                score= 1 * impact
            else:
                score= 0 * impact
                
            pair_score= get_pair_score(min= -6, max= 3, score=score)
            
        elif a == "Even" and b == "Fibonacci Number":
            impact= 1
            if (val_a and val_b) or (val_a != val_b):
                score= 1 * impact
            else:
                score= 0 * impact
            pair_score= get_pair_score(min= 0, max= 1, score=score)
            
        elif a == "Even" and b == "Perfect Square":
            impact= 1
            if (val_a and val_b) or (val_a != val_b):
                score= 1 * impact
            else:
                score= 0 * impact
            pair_score= get_pair_score(min= 0, max= 1, score=score)
        
        elif a == "Prime" and b == "Fibonacci Number":
            impact= 2
            if val_a != val_b:
                score= 1 * impact
            else:
                score= 0 * impact
            pair_score= get_pair_score(min= 0, max= 2, score=score)
            
        elif a == "Prime" and b == "Perfect Square":
            impact= 2
            if val_a and val_b:
                score= -1 * impact
            elif val_a != val_b:
                score= 1 * impact
            else:
                score= 0 * impact
            pair_score= get_pair_score(min= -2, max= 2, score=score)
            
        elif a == "Fibonacci Number" and b == "Perfect Square":
            impact= 2
            if val_a and val_b:
                score= -1 * impact
            elif val_a != val_b:
                score= 1 * impact
            else:
                score= 0 * impact
            pair_score= get_pair_score(min= -2, max= 2, score=score)
        
        else:
            print(f" Error in Pairs.\n Unknown a, b= {a}, {b}")
            
        benchmark += pair_score
    
    return benchmark

def main():
    main = ["Odd", "Prime", "Fibonacci Number", "Not Perfect Square"]
    confusion= ["Even", "Not Fibonacci Number"]
    mathmatical= ["Not Perfect Square", "Odd", "Prime"]
    
    main_bool = Converter(list=main)
    conf_bool = Converter(list=confusion)
    math_bool=Converter(list=mathmatical)
    
    #<======>Checker<======>
    mark1= Sanity_Check(subject=main, baseline=mathmatical)
    print("•Mark-1: Sanity Check:", mark1)
    
    mark2= Difficulty_Check(subject=math_bool, baseline=conf_bool)
    print("•Mark-2: Dificulty Check:", mark2)
    
    mark3= Pair_Check(subject=conf_bool)
    print("•Mark-3: Pair Evaluation Check:", mark3)
    
    print()
    print("—"*40)
    print(f"\n •Main List Bool: {main_bool}\n •Mathmatical Bool:{math_bool}\n •Confusional Bool:{conf_bool}")
    #print(f"\n Math List: {mathmatical}\n Confusional List: {confusion}")
    
main()