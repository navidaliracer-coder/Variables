# Students will use a Trivia API to fetch trivia questions and create an
# interactive quiz where they can answer the questions and receive feedback.

import requests
import random
import html

EDUCATION_CATEGORY_ID = 9

API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"


def get_education_questions():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        if data["response_code"] == 0 and data["results"]:
            return data["results"]

    return None


def run_quiz():
    questions = get_education_questions()

    if not questions:
        print("Failed to fetch the questions.")
        return

    score = 0

    print("=====================================")
    print(" Welcome to the Quiz of Everything!")
    print("=====================================\n")

    for i, q in enumerate(questions, start=1):

        question = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])

        # Combine correct and incorrect answers
        options = q["incorrect_answers"] + [q["correct_answer"]]
        options = [html.unescape(option) for option in options]

        # Shuffle the options
        random.shuffle(options)

        print(f"Question {i}:")
        print(question)

        # Display answer choices
        for j, option in enumerate(options, start=1):
            print(f"{j}. {option}")

        # Get user's answer
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        selected_answer = options[choice - 1]

        if selected_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was: {correct_answer}\n")

    print("=====================================")
    print("Quiz Complete!")
    print(f"Your final score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Outstanding! Perfect score!")
    elif percentage >= 80:
        print("Great job!")
    elif percentage >= 60:
        print("Nice work!")
    else:
        print("Keep practicing and try again!")


# Run the quiz
run_quiz()