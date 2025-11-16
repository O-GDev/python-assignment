first_player = input("Player 1; Enter \"rock\", \"paper\" or \"scissors\": ")
second_player = input("Player 2; Enter \"rock\", \"paper\" or \"scissors\": ")

if first_player.lower() == second_player.lower():
    print("Tie")
else:
    if first_player.lower() == "rock":
        if second_player.lower() == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif first_player.lower() == "paper":
        if second_player.lower() == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif first_player.lower() == "scissors":
        if second_player.lower() == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    else:
        print("Invalid input by Player 1")
