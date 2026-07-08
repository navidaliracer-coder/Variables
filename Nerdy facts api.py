import requests

url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_fact():
    response = requests.get(url)

    if response.status_code == 200:
        fact_data = response.json()   # <-- Missing ()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("failed to get that fact, srry twin")


while True:
    choice = input("Press enter to get a nerdy fact, or print 'q' if you have some resemblance of a life: ")

    if choice.lower() == 'q':
        break

    get_random_fact()   # <-- Missing ()