#!/usr/bin/env python3

def autism_screening():
    print("=== Autism Screening Questionnaire ===\n")
    print("This is a simple screening tool. Please answer the following questions honestly.")
    print("Note: This is NOT a medical diagnosis. Please consult a healthcare professional for proper evaluation.\n")

    score = 0
    total_questions = 10

    # Question 1
    print("1. Do you find it difficult to understand social cues or body language?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 2
    print("\n2. Do you have intense interests in specific topics that you can talk about for hours?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 3
    print("\n3. Do you prefer routine and get upset when plans change unexpectedly?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 4
    print("\n4. Do you find it challenging to maintain eye contact during conversations?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 5
    print("\n5. Do you have difficulty understanding sarcasm or jokes?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 6
    print("\n6. Do you experience sensory sensitivities (bright lights, loud sounds, certain textures)?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 7
    print("\n7. Do you find it hard to start or maintain conversations with others?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 8
    print("\n8. Do you prefer to spend time alone rather than in social situations?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 9
    print("\n9. Do you have difficulty understanding other people's emotions or feelings?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Question 10
    print("\n10. Do you engage in repetitive behaviors or movements (rocking, hand flapping, etc.)?")
    answer = input("Enter 'yes' or 'no': ").lower().strip()
    if answer == 'yes':
        score += 1

    # Calculate percentage
    percentage = (score / total_questions) * 100

    print(f"\n=== Results ===")
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")

    # Determine result using if-else statements
    if score <= 2:
        print("\nResult: LOW likelihood of autism")
        print("You show very few autistic traits. This is within the typical range.")
    elif score <= 4:
        print("\nResult: MILD likelihood of autism")
        print(
            "You show some autistic traits, but this is common in the general population.")
    elif score <= 6:
        print("\nResult: MODERATE likelihood of autism")
        print("You show several autistic traits. Consider consulting a healthcare professional.")
    elif score <= 8:
        print("\nResult: HIGH likelihood of autism")
        print("You show many autistic traits. It's recommended to seek professional evaluation.")
    else:
        print("\nResult: VERY HIGH likelihood of autism")
        print("You show most autistic traits. Professional evaluation is strongly recommended.")

    print("\n=== Important Disclaimer ===")
    print("This screening tool is for informational purposes only and cannot provide a medical diagnosis.")
    print("Autism is a complex neurodevelopmental condition that requires professional evaluation.")
    print("If you have concerns, please consult with a qualified healthcare provider, psychologist, or psychiatrist.")


if __name__ == "__main__":
    try:
        autism_screening()
    except KeyboardInterrupt:
        print("\n\nScreening interrupted. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try running the program again.")
