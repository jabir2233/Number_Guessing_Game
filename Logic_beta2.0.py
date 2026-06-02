import random
import os

#<======>Hint Checker<======>#
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
        
def divisible_by(num):
    hint = [ ]
    divisible_by = []
    for i in [2, 3, 5, 7]:
        if num % i == 0:
            divisible_by.append(str(i))
    if divisible_by:
        hint.append(f"divisible by {' and '.join(divisible_by)}")
        
    return hint
    
def perfect_square(num):
    if int(num**0.5) ** 2 == num:
        return True
    else:
        return False
    
def fibonacci_number(num):
    a, b= 0, 1
    while b < num:
        a, b= b, a+b
    return b==num or num==0
    
def math_hint_taker():
    hint= []
    num= number
    
    if is_even(num):
        hint.append("Even")
    else:
        hint.append("Odd")
        
    if is_prime(num):
        hint.append("Prime")
    else:
        hint.append("Not Prime")
        
    if fibonacci_number(num):
        hint.append("Fibonacci Number")
    else:
        hint.append("Not Fibonacci Number")
        
    if perfect_square(num):
        hint.append("Perfect Square")
    else:
        hint.append("Not Perfect Square")
        
    return hint
    
def confusional_hint(confusion_hint):
    if not confusion_hint:
        print("Error In Confusional Hint List.!")
        return
    #randomize the list
    c_hint = confusion_hint
    random.shuffle(c_hint)
    
    convert = {
            "Even":"Odd",
            "Odd":"Even",
            "Prime":"Not Prime",
            "Not Prime": "Prime",
            "Perfect Square":"Not Perfect Square",
            "Not Perfect Square":"Perfect Square",
            "Not Fibonacci Number":"Fibonacci Number",
            "Fibonacci Number":"Not Fibonacci Number"
    }
    
    counter = 0
    c_hint = [
    (counter := counter +1, convert[x])[1]
    if random.randint(1,3) <= 2 else x
    for x in c_hint
     ]
    
    if counter > 0:
        c_deduct = random.randint(0, counter)        
        counter -= c_deduct
        
    txt = f"Around {counter} Number of Hints Are Incorrect.!"
    if counter == 0:
        txt = f"Around 1 Or None of The Hints Are Incorrect.!"
        
    return c_hint, txt
  
def choice(math_hint, hint):
    attempts = 0
    
    while True:
        current = random.choice(math_hint)
        
        if current not in hint:
            return current
        
        attempts += 1
        
        if attempts > 10:
            print("Fallback triggered!")
            return current

def mathmatical_hint():
    math_hint = ["Even", "Not Prime", "Not Perfect Square", "Not Fibonacci Number"]
    math_hint = []
    math_hint= math_hint_taker()
    
    random.shuffle(math_hint)
    
    main_hint= list(math_hint)
    
    hint = []

    for i in range(3): 
        if not math_hint:
            break
        
        current =  choice(math_hint, hint)
        
        hint.append(current)
        luck = random.randint(1, 2)
        
        if luck == 1:
            math_hint.remove(current)
            #print("Removed from math_hint:", current)
        else:
            pass
            #print("Kept in math_hint:", current)
    
    confusion_hint = math_hint
    math_hint = hint
    
    return main_hint, math_hint, confusion_hint

def converter(list):
    text = ""
    i= 0
    for item in list:            
        i += 1
        text= f"{text} {item}"
        if i == (len(list)-1):
            text = text+" and"
        elif i == len(list):
            text = text+"."
        elif i > 0:
            text = text+","
        else:
            pass
    return(text)

def hint_organizer(number):
    hint_type = {
                        "hint_1": "propertical",
                        "hint_2": "confusional",
                        "hint_3": "propertical",
                        "hint_4": "mathmatical",
                        "hint_5": "propertical"
    }
    
    main_hint, math_hint, confusion_hint = mathmatical_hint()
    
    txt = None #Will Be Used To Print
    confusion_hint, txt= confusional_hint(confusion_hint)
    
    text= converter(list=math_hint)
    text= f"•Mathematical Hint:\n  {text}"
    hint_type["hint_4"]= text
    
    text= converter(list=confusion_hint)
    text= f"•{txt}\n  Hint:\n   {text}"
    hint_type["hint_2"]= text
    
#Main vs Mathmatical vs Confuisonal List
    return main_hint, math_hint, confusion_hint
    
#===Below Function Is Just A Demo===#
    c=1
    for type in hint_type:
        print("_"*42)
        print(f"  {hint_type[f"hint_{c}"]}")
        c+=1
        print("_"*42)
#===Avobe Function Is Just A Demo===#
