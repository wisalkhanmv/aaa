#!/usr/bin/env python3
import random


def autism_screening():
    print("=== Autism Screening Questionnaire ===\n")
    print("This is a simple screening tool. Please answer the following questions honestly.")
    print("Note: This is NOT a medical diagnosis. Please consult a healthcare professional for proper evaluation.\n")

    # Pool of autism screening questions
    all_questions = [
        "Do you find it difficult to understand social cues or body language?",
        "Do you have intense interests in specific topics that you can talk about for hours?",
        "Do you prefer routine and get upset when plans change unexpectedly?",
        "Do you find it challenging to maintain eye contact during conversations?",
        "Do you have difficulty understanding sarcasm or jokes?",
        "Do you experience sensory sensitivities (bright lights, loud sounds, certain textures)?",
        "Do you find it hard to start or maintain conversations with others?",
        "Do you prefer to spend time alone rather than in social situations?",
        "Do you have difficulty understanding other people's emotions or feelings?",
        "Do you engage in repetitive behaviors or movements (rocking, hand flapping, etc.)?",
        "Do you have difficulty with transitions between activities?",
        "Do you notice small details that others might miss?",
        "Do you have a strong need for sameness in your environment?",
        "Do you find it difficult to understand unwritten social rules?",
        "Do you have difficulty with flexible thinking or adapting to change?",
        "Do you experience anxiety in social situations?",
        "Do you have difficulty understanding metaphors or figurative language?",
        "Do you prefer to follow strict routines or schedules?",
        "Do you have difficulty with give-and-take conversations?",
        "Do you experience meltdowns when overwhelmed?",
        "Do you have difficulty understanding facial expressions?",
        "Do you prefer solitary activities over group activities?",
        "Do you have difficulty with time management?",
        "Do you experience difficulty with motor coordination?",
        "Do you have difficulty understanding personal space boundaries?",
        "Do you have difficulty with abstract thinking or conceptual reasoning?",
        "Do you experience difficulty with executive functioning (planning, organizing)?",
        "Do you have difficulty understanding nonverbal communication?",
        "Do you experience difficulty with emotional regulation?",
        "Do you have difficulty understanding social hierarchies or power dynamics?",
        "Do you experience difficulty with impulse control?",
        "Do you have difficulty understanding social reciprocity?",
        "Do you experience difficulty with theory of mind (understanding others' perspectives)?",
        "Do you have difficulty with pragmatic language skills?",
        "Do you experience difficulty with social imagination?",
        "Do you have difficulty understanding social context?",
        "Do you experience difficulty with social problem-solving?",
        "Do you have difficulty understanding social expectations?",
        "Do you experience difficulty with social adaptation?",
        "Do you have difficulty understanding social norms?",
        "Do you experience difficulty with social integration?",
        "Do you have difficulty understanding social relationships?",
        "Do you experience difficulty with social communication?",
        "Do you have difficulty understanding social boundaries?",
        "Do you experience difficulty with social reciprocity?",
        "Do you have difficulty understanding social cues?",
        "Do you experience difficulty with social timing?",
        "Do you have difficulty understanding social rules?",
        "Do you experience difficulty with social flexibility?",
        "Do you have difficulty understanding social context?",
        "Do you experience difficulty with social adaptation?",
        "Do you have difficulty understanding social expectations?",
        "Do you experience difficulty with social problem-solving?",
        "Do you have difficulty understanding social hierarchies?",
        "Do you experience difficulty with social imagination?",
        "Do you have difficulty understanding social relationships?",
        "Do you experience difficulty with social integration?"
    ]

    # Randomly select 10 questions and shuffle their order
    selected_questions = random.sample(all_questions, 10)
    random.shuffle(selected_questions)

    score = 0
    total_questions = len(selected_questions)

    # Ask the randomly selected questions
    for i, question in enumerate(selected_questions, 1):
        print(f"{i}. {question}")
        answer = input("Enter 'yes' or 'no': ").lower().strip()
        if answer == 'yes':
            score += 1
        print()  # Add spacing between questions

    # Calculate percentage
    percentage = (score / total_questions) * 100

    print(f"\n=== Results ===")
    print(f"Your score: {score}/{total_questions} ({percentage:.1f}%)")

    # Determine result using if-else statements with detailed explanations
    if score <= 2:
        print("\nResult: LOW likelihood of autism")
        print("You show very few autistic traits. This is within the typical range.")
        print("\nReasons for this result:")
        print("• Your responses indicate typical social communication patterns")
        print("• You show good understanding of social cues and expectations")
        print("• Your sensory processing appears to be within normal ranges")
        print("• You demonstrate flexible thinking and adaptability")
        print("• Your social interactions follow typical patterns")

    elif score <= 4:
        print("\nResult: MILD likelihood of autism")
        print(
            "You show some autistic traits, but this is common in the general population.")
        print("\nReasons for this result:")
        print("• You may have slight difficulties in certain social situations")
        print("• Some sensory sensitivities or preferences may be present")
        print("• You might prefer routine in some areas of life")
        print("• These traits are common and don't necessarily indicate autism")
        print("• Many people have similar experiences without being autistic")

    elif score <= 6:
        print("\nResult: MODERATE likelihood of autism")
        print("You show several autistic traits. Consider consulting a healthcare professional.")
        print("\nReasons for this result:")
        print("• You demonstrate multiple characteristics commonly associated with autism")
        print("• Your social communication patterns show some differences")
        print("• Sensory sensitivities or repetitive behaviors may be more noticeable")
        print("• These traits may be affecting your daily life")
        print("• Professional evaluation could help clarify your experiences")

    elif score <= 8:
        print("\nResult: HIGH likelihood of autism")
        print("You show many autistic traits. It's recommended to seek professional evaluation.")
        print("\nReasons for this result:")
        print("• You display a significant number of autistic characteristics")
        print("• Your social communication shows clear differences from typical patterns")
        print("• Sensory sensitivities and repetitive behaviors are likely present")
        print("• These traits probably impact your daily functioning")
        print("• Professional assessment is strongly recommended for proper support")

    else:
        print("\nResult: VERY HIGH likelihood of autism")
        print("You show most autistic traits. Professional evaluation is strongly recommended.")
        print("\nReasons for this result:")
        print("• You display the majority of autistic characteristics assessed")
        print("• Your social communication patterns are significantly different")
        print("• Sensory processing differences are likely substantial")
        print("• These traits are probably significantly impacting your life")
        print("• Immediate professional evaluation is highly recommended")
        print("• Early diagnosis can lead to better support and accommodations")

    print("\n=== What This Means ===")
    print("• Higher scores indicate more autistic traits, not necessarily autism itself")
    print("• Many people have some autistic traits without being autistic")
    print("• Environmental factors, anxiety, or other conditions can cause similar traits")
    print("• Only a qualified professional can provide an accurate diagnosis")
    print("• This screening is just one tool to help guide your next steps")

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
