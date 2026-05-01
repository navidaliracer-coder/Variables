import re, random
from colorama import Fore, init

init(autoreset = True)

destinations = {
    "Beaches": ["Dominican Republic", "Miami", "Cancun"],
    "Hikes": ["Rocky Mountains", "Grand Canyon", "Pacific crest trail"],
    "Cities": ["Toronto", "New York", "Mexico City"],


}

jokes = [
    "What is the Jokers favroite bread?, Rye so serious!"
    "Why can't the orphan play baseball? It can't find home!"
    "Why did the programer not want to go pn a hike? Because there were to many bugs!"

]

def normalize_input (text):
    return re.sub(r"\s+", "", text.strip().lower)

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, Mountains, Or cities")
    preference = input(Fore.YELLOW + "You:")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestions = random.choices(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestions}?")
        print(Fore.YELLOW + "You: ").lower()

        if answer == "Yes":
            print(Fore.GREEN + f"TravelBot: Awesome, Enjoy {suggestions}")
        elif answer == "No":
            print(Fore.RED + "TravelBot: I will suggest again.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Sorry, please rephrase")

