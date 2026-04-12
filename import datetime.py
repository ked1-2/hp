import datetime

def mood_tracker():
    # Define a simple mood menu
    mood_options = {
        "1": "Excellent (Feeling great!)",
        "2": "Good (Productive/Calm)",
        "3": "Neutral (Just okay)",
        "4": "Low (Tired/Stressed)",
        "5": "Difficult (Anxious/Sad)"
    }

    print("--- Daily Mood Tracker ---")
    print(f"Today is: {datetime.date.today()}\n")
    
    for key, value in mood_options.items():
        print(f"{key}. {value}")

    # Get user input
    choice = input("\nHow are you feeling today? (1-5): ")
    
    if choice in mood_options:
        mood_label = mood_options[choice]
        note = input("Add a quick note about your day (optional): ")
        
        # Format the entry
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"[{timestamp}] Mood: {mood_label} | Note: {note}\n"

        # Save to a text file
        try:
            with open("mood_log.txt", "a") as file:
                file.write(entry)
            print("\nMood logged successfully! Keep up the great work.")
        except Exception as e:
            print(f"Error saving mood: {e}")
    else:
        print("Invalid choice. Please run the script again and select 1-5.")

if __name__ == "__main__":
    mood_tracker()