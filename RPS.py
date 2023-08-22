from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3



while player_wins < winning_score and computer_wins < winning_score:
	print(f"player score:{player_wins} Vs Computer score:{computer_wins}")
	player = input("pl1, MakE mv:")
	if player == "quit" or player == "q":
		break		
	rand_num = randint(0,3)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
	    computer = "paper"
	else:
	    computer = "scissors"
	print(f"computer plays {computer}")
	if player == computer:
	    print("its a tie")
	elif player == "rock":
		if computer == "scissors":
			print("player wins")
			player_wins += 1
		elif computer == "paper":
			print("computer wins")
			computer_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("player1 wins")
			player_wins += 1
		elif computer == "scissors":
			print("computer wins")
			computer_wins += 1
	elif player == "scissors":
		if computer == "paper":
			print("player1 wins")
			player_wins +=1
		elif computer == "rock":
			print("computer wins")
			computer_wins += 1
	else:
		print("something wrong")
	
	
print(f"final score.....player score:{player_wins} Vs Computer score:{computer_wins}")
if player_wins > computer_wins:
	print("COngrates U won")
elif player_wins == computer_wins:
	print("Its a Tie")
else:
	print("YOU lost")


		
			
			
   
	    
		    
		    
    
	    


    

    