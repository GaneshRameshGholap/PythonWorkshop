word ="Welcome"
print(word[0]+"----"+word[-1])
guesses=0
turns =len(word)-2
failed=0
while turns > 0:         
    guess =input("Enter the character for Guessing:")  
    if guess in word:          
            print (guess)
            guesses+=1
            if(guesses==(len(word)-2)):
                 print("You Won the Game:")
                 break                           
    if guess not in word: 
        failed+=1 
        turns -= 1           
        print ("Wrong You have", + turns, 'more guesses') 
        if turns == 0:           
            print (f"You Loose your score will be {guesses}")  