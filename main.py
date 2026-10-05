from groq import generate_response

def reinforcement_learning_activity():
    print("\n=== Reinforcement Learning Activity ===\n")
    prompt = ("Enter a prompt for the ai model (e.g ' discribe a lion in the jungle'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial Response:\n{initial_response}\n")

    try:
        rating = int(input("Rate the response from 1 (worst) to 5 (best): ").strip())
        if rating < 1 or rating > 5:
            print  ("Invalid rating. using 3 as default.")
            rating = 3
    except ValueError:
        print("Invalid input. using 3 as default.")
        rating = 3
    
    feedback = input ("Please provide feedback for the model's response: ").strip()
    imporved_prompt = f"{prompt}\n\nThe user rated the response {rating}/5 and provided the following feedback: {feedback}\n\nPlease provide an improved response based on this feedback."
    print(f"\nImproved AI response:\n{imporved_prompt}\n")

    print("\nReflection: The model's response was rated and feedback was provided. This feedback can be used to improve future responses.")
    print("1. How did the models response improve based on the feedback provided?")
    print("2. What specific changes did you notice in the improved response?")

def role_based_prompt_activity():
    print("\n=== Role-Based Prompt Activity ===\n")
    category = input("Enter a category for the role-based prompt (e.g., 'doctor', 'teacher', 'chef'): ").strip()
    item = input("Enter a specific {category} item (e.g., 'medical advice', 'lesson plan', 'recipe'): ").strip()

    if not category or not item:
        print("Please enter both a category and an item to run the activity.")
        return
    
    teacher_prompt = f"Imagine you are a {category}. Please provide a detailed {item} that would be useful for someone seeking advice or information in this area."
    expert_prompt = f"Imagine you are an expert {category}. Please provide an in-depth and professional {item} that would be valuable for someone looking for expert guidance in this field."

    teacher_prompt = generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_prompt = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)
    
    print(f"\nResponse from a {category}:\n{teacher_prompt}\n")
    print(f"\nResponse from an expert {category}:\n{expert_prompt}\n")

    print("\nReflection: The responses from both the general and expert roles were generated. Consider the differences in depth, detail, and perspective between the two responses.")
    print ("2. How did the expert response differ from the general response in terms of detail and insight?")

def run_activty():
    print("Welcome to the AI Model Activities!")
    print("Choose an activity to run:")
    print("1. Reinforcement Learning Activity")
    print("2. Role-Based Prompt Activity")
    choice = input("Enter the number of the activity you want to run (1 or 2): ").strip()

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    run_activty()
 
