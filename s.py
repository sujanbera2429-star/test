while True:
    print("\n===== Daily Notes App =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

            if notes:
                print("\n===== Saved Notes =====")
                print(notes)
            else:
                print("No notes found.")

        except FileNotFoundError:
            print("No notes found.")

    elif choice == "3":
        print("Exiting Daily Notes App. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
