from time import time


# This Project Was Inspired From "Tech With Tim" From Youtube!

print("Welcome to my computer quiz")

playing = input("Do You want to play? ")



if playing.lower() != "yes":
        quit()

print("Okay! Lets play :)")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What Does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What Does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What Does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    print("You got " + str((score / 4) * 100) + "%")
    

    

