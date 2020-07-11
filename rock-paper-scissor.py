import random
lst=['r','p','s']

total_chances=10
chance=0
computer_point=0
human_point=0

print("\t\t\t Rock,paper&scissor game\n \n ")
print("r for rock \n p for paper \n s for scissor")


while chance < total_chances:
    _input=input('rock,paper,scissor:')
    _random = random.choice(lst)
    
    if _input==_random:
        print("tie  0 point to both\n")
        
    #if user enters r
    elif _input=="r" and _random=="p":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input=="r" and _random=="s":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    # if user enters p
    elif _input=="p" and _random=="s":
        computer_point=computer_point+1
        print(f"your guess {_input} and computer guessis {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input=="p" and _random=="r":
        human_point=human_point+1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enters s
    elif _input=="s" and _random=="p":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("human wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input=="s" and _random=="r":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    else:
        print("you have wrong input \n")

    chance=chance+1
    print(f"{total_chances - chance} is left out of {total_chances} \n")

print("game over")

if computer_point>human_point:
    print("computer wins and you lose")
    
if computer_point<human_point:
    print("you wins and computer lose")
    
print(f"your point is {human_point} and computer_point is {computer_point}") 
    
    


    
