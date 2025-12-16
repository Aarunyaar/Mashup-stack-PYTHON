try:

    name = input("Enter your name: ").strip()
    feedback = input("Enter your feedback: ").strip()


    if not name:
        raise ValueError("Error: Name cannot be empty.")
    if not feedback:
        raise ValueError("Error: Feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print(e)

except Exception:
    print("An unexpected error occurred.")

finally:
    print("\nWe appreciate you taking the time to share your thoughts.")