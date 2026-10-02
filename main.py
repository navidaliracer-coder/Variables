from groq import generate_response

def run_activity():
    print("Zero Shot, One shot, few shot, learning activity")

    category = input("Enter a category (e.g animal, food, city)").strip()
    item = input   ("Enter an item in that {category} (e.g dog, pizza, Paris)").strip() 

    if not category or not item:
        print("Please fill in both fields to run the activty")  
        return
    
    zero_shot = f"Is {item} a {category}? Answer with yes or no."
    print("\n Zero Shot Learning")
    print(f"Response {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot = f"""Example: Is a dog an animal? Yes.
Question: Is {item} a {category}? Answer with yes or no."""
    print("\n One Shot Learning")
    print(f"Response {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot = f"""Example: Is a dog an animal? Yes.
Example: Is a pizza a food? Yes.
Question: Is {item} a {category}? Answer with yes or no."""
    print("\n Few Shot Learning")
    print(f"Response {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

if __name__ == "__main__":
    run_activity()
    







