import random

secret_num = random.randint(1,10)

while True: 
    guess = int(input("Guess a number between 1 and 10: "))
            
    if guess == secret_num:
        print("You have a good number!")
        break
    
    else:
        print("You are wrong")
                                                        
                                                                      
