try:
    # Ask user for book title
    title = input("Enter book title: ")

    # Validate title (only alphabets and spaces)
    if not title.replace(" ", "").isalpha():
        raise ValueError("Error: Book title must contain only alphabets and spaces.")

    # Ask user for publication year
    year = input("Enter publication year: ")

    # Validate year (4 digits and starts with 19 or 20)
    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Publication year must be a 4-digit number starting with 19 or 20.")

    # If everything is valid
    print("\nBook details accepted successfully!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

except Exception:
    print("An unexpected error occurred.")

finally:
    print("\nThank you for using the mini library system.")