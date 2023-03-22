
import random

Level = { "beginer" : 5,
          "intermediate" : 3,
          "advanced" : 1
        } 

print(Level["beginer"])

Save = ""

PlayAgian = ""

HighestScore = {} # the highest score dictionary

while True: # the game logic
    UserLevel = input("Enter your level : ") 
    Score = 0
    choices = Level[UserLevel.lower()] if UserLevel.lower() in Level   else 0
    print("You had ",choices," choices")
    if choices > 0 :
        while (True):
            Number = int( input("Enter a number : ") )
    
            if Number == random.randint(0,9):
                Score += 1 if UserLevel.lower() == "beginer" else 3 if UserLevel.lower() == "intermediate" else 5
                print('Correct Guess \n your score : ',Score)

            else:
                choices -= 1
                print('Wrong Guess \n you had ' ,choices, " choices")

            if choices == 0:
                print('Game Over! \n Your final score : ',Score,' \n Do you want to save your score?(Y/N): ')
                Save = input()
                break  

    else:
        print("ERROR: 404")
       
    if Save.upper() == 'Y': # Saving the final score
        Name = input("Enter the name : ")
        HighestScore[Name] = Score
        print("Thanks for playing. \n Do you want to play again? (Y/N): ")
        PlayAgian = input()
    else:
        print("Thanks for playing. \n Do you want to play again? (Y/N): ")
        PlayAgian = input()

    if PlayAgian.lower() == 'n': # Exit
        break

print("previous High Score holders : ")   # High Score holders
print(*[str(k) + ':' + str(v) for k,v in HighestScore.items()])  
