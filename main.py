import random

'''
Snake Water Gun Game

Snake = 1
Water = -1
Gun = 0
'''

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s = Snake, w = Water, g = Gun): ").lower()

youdict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reversedict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Check for invalid input
if youstr not in youdict:
    print("Invalid Choice!")
    exit()

you = youdict[youstr]

print(f"\nYou chose: {reversedict[you]}")
print(f"Computer chose: {reversedict[computer]}\n")

if computer == you:
    print("🤝 It's a Tie!")

elif (you == 1 and computer == -1):      # Snake beats Water
    print("🎉 You Win!")

elif (you == -1 and computer == 0):      # Water beats Gun
    print("🎉 You Win!")

elif (you == 0 and computer == 1):       # Gun beats Snake
    print("🎉 You Win!")

else:
    print("😔 You Lose!")