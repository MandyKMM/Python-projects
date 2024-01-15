import random

user = int(input("Choose 0 for rock, 1 for paper and 2 for scissors.\n"))
rock = "=0"
paper = "=[]"
scissors = "=K"
rps = [rock, paper, scissors]

computer = random.randint(0, 2)

if not (0 <= user <= 2):
    print("Invalid")
elif (user == 0 and computer == 1) or (user == 1 and computer == 2) or (user == 2 and computer == 0):
    print(f"\n{rps[user]}\n")
    print(f"computer chose:\n{rps[computer]}\n")
    print("You lose")
elif user == computer:
    print(f"\n{rps[user]}\n")
    print(f"computer chose:\n{rps[computer]}\n")
    print("Draw")
else:
    print(f"\n{rps[user]}\n")
    print(f"computer chose:\n{rps[computer]}\n")
    print("You win")
