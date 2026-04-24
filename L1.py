print("Hello, I am an AI bot! Whats your name?:    ")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) :")
mood = input().lower()

if mood == "good":
    print("I am glad to hear that!")
elif mood == "bad":
    print("Sorry to hear that, hope life improves soon!")
else:
    print("I see, sometimes it is hard to put your feelings into moods!")


print(f"Nice chatting with you!")

