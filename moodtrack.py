from datetime import date

def log_mood():
    mood = input("How are you feeling today? (e.g., happy, tired, anxious): ")
    note = input("Any reason or mood swing you'd like to note?: ")
    
    with open("mood_log.txt", "a") as file:
        file.write(f"{date.today()} - Mood: {mood} | Note: {note}\n")
    
    print("Mood and note saved successfully!")

log_mood()