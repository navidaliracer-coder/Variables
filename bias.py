# Explore Bias Mitigation and Token Limits in AI

from groq import generate_response

def bias_mitigation_activity():
    print("\n=== Bias Mitigation Activity ===")
    prompt = input("Enter a prompt to test for bias: ").strip()

    if not prompt:
        print("No prompt provided. Please try again.")
        return

    initial_response = generate_response(
        prompt, temperature=0.3, max_tokens=1024
    )
    print(f"\nInitial Response:\n{initial_response}")

    modified_prompt = input(
        "\nRewrite the prompt to request a balanced, unbiased response: "
    ).strip()

    if modified_prompt:
        neutral_response = generate_response(
            modified_prompt, temperature=0.3, max_tokens=1024
        )
        print(f"\nModified Response (neutral):\n{neutral_response}")
    else:
        print("No modified prompt provided. Skipping this step.")

def token_limit_activity():
    print("\n=== Token Limit Activity ===")
    long_prompt = input("Enter a long prompt to test token limits: ").strip()

    if not long_prompt:
        print("No prompt provided. Please try again.")
        return

    response = generate_response(
        long_prompt, temperature=0.3, max_tokens=1024
    )
    print(f"\nResponse (maximum 1024 tokens):\n{response}")
    print("\nNote: The response may be shorter than the token limit.")

def main():
    while True:
        print("\n=== AI Response Generation ===")
        print("1. Bias Mitigation")
        print("2. Token Limits")
        print("3. Exit")

        choice = input("Choose an activity (1-3): ").strip()

        if choice == "1":
            bias_mitigation_activity()
        elif choice == "2":
            token_limit_activity()
        elif choice == "3":
            print("Activity complete. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()