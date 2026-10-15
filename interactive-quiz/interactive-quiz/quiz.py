print("===== Computer Science Quiz =====")

name = input("What is your name? ")
print("Good luck, " + name + "!")

score = 0

print("Q1: Which language are we learning?")
print("A. Java")
print("B. Python")
print("C. HTML")

answer = input("Your answer (A/B/C): ")

if answer.lower() == "b":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("Q2: What does CPU stand for?")
print("A. Central Processing Unit")
print("B. Computer Personal Unit")
print("C. Central Processing Utility")

answer = input("Your answer (A/B/C): ")

if answer.lower() == "a":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

percentage = (score / 2) * 100

print("===== RESULTS =====")
print("Player:", name)
print("Your Score is:", score, "/ 2")
print("Your Percentage is", percentage, "%")
