print('Hello! Welcome to my history quiz!')

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Ok! Let's play!")
score = 0

answer = input('When did World War II started? ')
if answer == "1939":
    print("Correctly! World War II began on September 1, 1939, with the German invasion of Poland.")
    score += 1
else:
    print("Incorrect!")

answer = input("When did the October Revolution take place? ")
if answer == "1917":
    print("Correctly!")
    score += 1
else:
    print("Incorrect!")
    
answer = input('When did the French Revolution take place? ')
if answer == "1789":
    print("Correctly! French Revolution was a period of radical social and political upheaval in France.")
    score += 1
else:
    print("Incorrect!")

answer = input('Who was the first female British Prime Minister? ')
if answer.lower() == "margaret thatcher":
    print("Correctly!")
    score += 1
else:
    print("Incorrect!")

answer = input("When did World War I end? ")
if answer == "1918":
    print("Correctly! After more than four years of horrific fighting.")
    score += 1
else:
    print("Incorrect!")
    

print("You got " +str(score) + " questions correct!")
print("You got " +str((score/5) * 100) + "%")