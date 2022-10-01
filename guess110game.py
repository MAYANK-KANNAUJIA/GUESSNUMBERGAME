import random as r
cpu=r.randint(1,10)
print("RANGE 1 TO 10")
counter=3
game=True
while game:
    num=int(input("ENTER NUMBER="))
    if(num==cpu):
        print("CONGRATULATIONS!!!!! YOU WON")
        print("number was",num)
        break
    elif(num>cpu):
        print("YOU GUESSED GREATER NUMBER")
        counter=counter-1
        print("chances left",counter)
        if(counter>0):
            game=True
        else:
            game=False
        

    elif(num<cpu):
        print("YOU GUESSED SMALLER NUMBER")
        counter=counter-1
        print("chances left",counter)
        if(counter>0):
            game=True
        else:
            game=False
        
else:
    print("YOU LOOSE")
    
