# PERSONALIZED GREETING APP

def greetings():
    name = input("Enter your name: ")
    favorite_color = input("Enter your favorite color: ")
    print("Hello, " + name + "! Your favorite color, " + favorite_color + ", is awesome.")

greetings()


#SIMPLE QUIZ GAME
def game():
    print("Welcome to Mercy's game!!")
    print("Answer the following questions correctly to win points.")
    print("ENSURE TO CAPITALIZE YOUR LETTERS OR REWRITE THE ANSWERS LIKE WRITTEN")
    print("Good luck!")
    print("Question 1: What is the capital of Nigeria?")
    print("A. Lagos")
    print("B. Laos")
    print("C. Nairobi")
    print("D. Abuja")
    answer1 = input("Enter your answer: ")
    if answer1 == "Abuja" or answer1 == "D":
        print("Correct!You earned 5 points")
    else:
        print("Wrong answer! No points for you.")
        print("The correct answer is Abuja.")

    print("Question 2: Do cockroaches have wings?")
    print("A. Yes")
    print("B. No")

    answer2 = input("Enter your answer: ")
    if answer2 == "Yes" or answer2 == "A":
        print("Look at you go!You earned 5 points")
    else:
        print("Wrong answer! No points for you.")
        print("The correct answer is Yes cockroaches have wings.")    

    
    print("Question 3: What is your favourite country?")
    answer3 = input("Enter your answer: ")
    print("Nice choice! You earned 5 points")
    print("You have completed the game. Thanks for playing.")

game()

# RANDOM JOKE GENERATOR
print("Before you go, here's a joke for you!")

def joke():
    import random
    jokes = ["Why did the tomato turn red? Because it saw the salad dressing!",
             "Why did the scarecrow win an award? Because he was outstanding in his field!",
             "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
             "Why did the math book look sad? Because it had too many problems!",
             "Why did the cookie go to the doctor? Because it was feeling crumbly!"]
    print(random.choice(jokes))

joke()

# FULL SAYINGS
print("Ok OK, I know you are leaving but here is a saying for you!!")
print("The saying might be a SIGNN!!")
print("YOU CAN NEVER TELL!!")
import random
def sayings():
    sayings=["Curiosity killed the cat, but satisfaction brought it back.",
            "Blood is thicker than water, but the blood of the covenant is thicker than the water of the womb.",
            "The early bird catches the worm, but the second mouse gets the cheese.",
            "The pen is mightier than the sword, but actions speak louder than words.",
            "Great minds think alike, but fools seldom differ.",
            "Practice makes perfect, but nobody's perfect.",
            "Better safe than sorry, but never say never.",
            "Money is the root of all evil, but the love of money is the root of all evil.",
            "An apple a day keeps the doctor away, but if the doctor is cute, forget the fruit.",
            "Idle hands are the devil’s workshop, but busy hands are God’s playground.",
            "Speak of the devil, and he shall appear. But if you talk about someone long enough, they will appear.",
            "The best things in life are free, but there's no such thing as a free lunch.",
            "Absence makes the heart grow fonder, but out of sight, out of mind.",
            "Beauty is in the eye of the beholder, but ugly goes straight to the bone.",
            "Too many cooks spoil the broth, but many hands make light work.",
            "When in Rome, do as the Romans do, but all roads lead to Rome.",
            "When life gives you lemons, make lemonade—but if you don’t have sugar, it’ll still be sour."
             ]
    print(random.choice(sayings))
sayings()
print("Thank you for playing. Goodbye!!")
    

    
