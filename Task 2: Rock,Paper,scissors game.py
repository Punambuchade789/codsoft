import random
possible_actions = ["rock", "paper", "scissors"]
running=True

while running:
  user =None
  computer = random.choice(possible_actions)
  
  while user not in possible_actions:
       user = input("Enter a choice (rock, paper, scissors): ")
       print(f"user:{user}")
       print(f"computer: {computer}")
       if user == computer:
            print("It's a tie")
       elif user =="rock" and computer=="scissors":
        print("You win!")    
       elif user== "paper" and computer=="rock":
         print("You win!")  
       elif user=="scissors" and computer =="paper":
         print("You win!")    
       else:
        print("You lose.")
       play_again = input("Play again? (y/n): ").lower()
       if  not play_again == "y":
          running=False
        
print("thanks for playing")        
        
