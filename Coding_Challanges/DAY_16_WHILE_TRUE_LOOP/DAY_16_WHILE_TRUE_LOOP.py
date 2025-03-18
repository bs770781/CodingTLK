# Davids Example Colour Game
while True:
    print("This program is running")

    goAgain = input("Do you want to continue? (yes/no): ").lower()
    if goAgain == "no":
        break

print("Aww, I was having a good time")
# Bilals Example
while True:
    color = input("What's your favorite color? ").lower()

    responses = {
        "blue": "Great choice! Blue is a calming color.",
        "red": "Red is so energetic and bold!",
        "green": "Green is so peaceful and refreshing!"
    }

    print(responses.get(color, "Nice! That's a unique color."))

    if input("Do you want to tell me another color? (yes/no): ").lower() == "no":
        break
print("Thanks for sharing your colors with me!")



