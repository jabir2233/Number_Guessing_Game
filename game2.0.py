from candidate_generator_beta import hint_organizer
from candidate_checker import hint_grader
import random

def main():
    number= random.randint(0,100)
    
    main_hint, math_hint, confusion_hint= hint_organizer(number)
    
    mark1, mark2, mark3= hint_grader(main_hint, math_hint, confusion_hint)
    
    print("—"*40)
    print(f"  •Main Hint List: {main_hint},\n  •Math Hint List: {math_hint} &\n  •Confusional Hint List: {confusion_hint}\n")
    print("—"*40)
    print(f"  •Mark-1: {mark1}, •Mark-2: {mark2} & •Mark-3: {mark3}")
    print("—"*40)
    
if __name__ == "__main__":
    for i in range(0,9):
        main()