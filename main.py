import random
names = {
    "s" : "Snake",
    "w" : "Water",
    "g" : "Gun"
}

computer = random.choice(["s", "w", "g"])
print("Snake, Water or Gun")
user = input("Enter your choice: ").lower()

if user in ["s", "w", "g"]:
    print("Computer chose: ", names[computer])
    print("User chose: ", names[user])
    if(user == computer):
        print("Draw")
    elif(user == "s" and computer == "w"):
        print("You won")
    elif(user == "w" and computer == "g"):
        print("You won")
    elif(user == "g" and computer == "s"):
        print("You won")
    else:
        print("You Lose")
else:
    print("Invalid Input")