import random
from flask import Flask, render_template, request, session, redirect

Game = Flask(__name__)
Game.secret_key = 'Jabir2233'


@Game.route("/", methods=["GET", "POST"])
def home():
    #Debug

    # Initialize session only once
    if "game" not in session:
        print("New Session is Created.")
        session["game"] = {
            "state": "menu",
            "number": None,
            "attempts": 0
        }

    game = session["game"]
    
    
    if error_session():
        print("Session Is Live!")
        return "Session isn't Created!"

    if request.method == "POST":
        action = request.form.get("action")

        # ▶ PLAY BUTTON
        if action == "play":
            game["state"] = "playing"
            game["number"] = random.randint(1, 100)  # secret number
            game["attempts"] = 0

        # ▶ SUBMIT GUESS
        elif action == "submit":
            guess = request.form.get("guess")

            if guess:
                txt_p = valuate_attempt(guess)
                session["last_hint"] = txt_p   # store hint
                
        # Restart Game
        elif action == "restart":
            session.pop("last_hint", None)
            session["game"] = {
            "state": "playing",
            "number": random.randint(1,100),
            "attempts": 0
            }
            return redirect("/")
            
        # Play -> Menu
        elif action == "menu":
            session.clear()
            return redirect("/")
            
        else:
            return "Invalid Action Type"

        session["game"] = game  # save changes

    # UI rendering
    txt_t, txt_p = workflow()

    return render_template(
        "home.html",
        state=game["state"],
        text_h=txt_t,
        text_p=txt_p
    )


# -------- UI WORKFLOW -------- #

def workflow():
    game = session["game"]
    state = game["state"]

    if state == "menu":
        print("Current State: Menu")
        txt_t = "Introduction & Rules"
        txt_p = (
            "Welcome to The Number Guessing Game!<br>"
            "The Computer Chose A Number Between 1 and 100<br>"
            "You Have 4 Attempts + Final Chance<br>"
            "Hints Will Help You!"
        )
        return txt_t, txt_p

    elif state == "playing":
        print("Current State: Playing")
        txt_t = "Hints"
        
        attempt_no = session["game"]["attempts"]
        attempt_no += 1
        
        # show last hint if exists
        txt_p = session.get("last_hint", "What's Your First Guess?")
        
        if attempt_no != 0:
            txt_p = f"Attempt:{attempt_no}: {txt_p}"
            
        print(txt_p)

        return txt_t, txt_p

    elif state == "result":
        print("Current State: Result")
        txt_t = "Game Over"
        txt_p = session.get("last_hint", "Result shown here")
        return txt_t, txt_p

    return "Error", "Invalid state"


#---------- Final Hint ----------#

# Function to check if a number is prime
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
    
# Function to generate a detailed hint based on number properties
def get_final_hint(number):
    hint = [ ]

    # Even or Odd Hint
    if is_even(number):
        hint.append("even")
        print("Even Number")
    else:
        hint.append("odd")
        print("Odd Number")

    # Prime Number Hint
    if is_prime(number):
        hint.append("prime")
        print("Prime Number")
        
    #Fibonacci Number Hint
    if fibonacci_number(number):
        hint.append("fibonacci number")
        print("Fibonacci Number")
    
    #Perfrct Square Hint
    if perfect_square(number):
        hint.append("perfect square")
        print("The Number is Perfect Square")

    # Divisibility Hint
    hint.append(divisible_by(number))
    
    return hint
#---------- GAME LOGIC ----------#          
def valuate_attempt(guess):
    try:
        guess = int(guess)
        game = session["game"]

        number = int(game["number"])
        attempt = game["attempts"] + 1
        
        game["attempts"] = attempt
        
        print(attempt)

        if guess < number:
            diff = number - guess

            if diff > 20:
                a = random.randint(1, 4)

                if a == 1:
                    hint = "The Number Is Much Higher!"
                elif a == 2:
                    hint = "Way Too Low! Try Much Higher."
                elif a == 3:
                    hint = "You Need To Climb Higher."
                elif a == 4:
                    hint = "Not Even Close. Go Higher!"

            elif diff > 10:
                b = random.randint(1, 3)

                if b == 1:
                    hint = "The Number Is Higher."
                elif b == 2:
                    hint = "Good Try! Increase It A Bit More."
                elif b == 3:
                    hint = "You're Getting Closer. Try Slightly Higher."

            else:
                    c = random.randint(1, 3)
                    if c == 1:
                        hint = "You're Very Close Now!"
                    elif c == 2:
                        hint = "Almost There... Think About '+'"
                    elif c == 3:
                        hint = "Just A Tiny Bit Higher."

        elif guess > number:
            diff = guess - number

            if diff > 20:
                a = random.randint(1, 4)

                if a == 1:
                    hint = "The Number Is Much Lower!"
                elif a == 2:
                    hint = "Way Too High! Try Lower."
                elif a == 3:
                    hint = "Go Down Much More."
                elif a == 4:
                    hint = "Not Even Close. Try Lower!"

            elif diff > 10:
                b = random.randint(1, 3)

                if b == 1:
                    hint = "The Number Is Lower."
                elif b == 2:
                    hint = "Nice Guess! Reduce It A Little."
                elif b == 3:
                    hint = "You're Getting Closer. Try Slightly Lower."

            else:
                c = random.randint(1, 3)

                if c == 1:
                    hint = "You're Very Close Now!"
                elif c == 2:
                    hint = "Almost There... Think About '-'"
                elif c == 3:
                    hint = "Just A Tiny Bit Lower."
        else:
            game["state"] = "result"
            
            print("Player Won The Game")
            print("Deleting Session")
            session.pop("game")
            session.pop("last_hint", None)
            print("Session Deleted:")
            print(error_session())
            
            return "🎉 Congratulations! You guessed correctly!"
            
        #Return Hint or Final Hint
        #Final Attempt 
        if attempt == 4:
            final_hint = get_final_hint(number)
            final_hint = f"{hint}. Moreover,The Number is: {final_hint}"
            return final_hint
            
        #Game Over
        if attempt >= 5:
            game["state"] = "result"
            
            print("Player Loses The Game")
            print("Deleting Session")
            session.pop("game")
            session.pop("last_hint", None)
            print("Session Deleted:")
            print(error_session())
            
            return f"You Lost The Game. The Number is:{number}"
            
        return hint

    except ValueError:
        return "Invalid input. Enter a number."


# ------- SESSION CHECK ------ #

def error_session():
    if "game" not in session:
        print('Error in Session')
        return True

    game = session["game"]

    if "state" not in game:
        return True
    elif "number" not in game:
        return True
    elif "attempts" not in game:
        return True

    return False


if __name__ == "__main__":
    Game.run()
