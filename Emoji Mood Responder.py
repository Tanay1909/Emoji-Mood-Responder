# Step 1: Create a dictionary mapping moods to emojis and messages
MOOD_RESPONSES = {
    "happy":    ("😊", "Glad to see you're happy!"),
    "sad":      ("😢", "Sorry you're feeling sad."),
    "angry":    ("😡", "Take a deep breath."),
    "surprised":("😱", "Wow! That was unexpected!"),
    "sleepy":   ("😴", "Time for a nap?"),
    "laughing": ("😂", "Laughter is the best medicine!"),
    "love":     ("😍", "Love is in the air!"),
    "thinking": ("🤔", "Deep thoughts, huh?"),
    "cool":     ("😎", "Looking cool!"),
    "crying":   ("😭", "It's okay to cry sometimes.")
}

# Step 2: Ask the user for their mood
user_mood = input("How are you feeling today? ").strip().lower()

# Step 3 & 4: Match mood and print response
if user_mood in MOOD_RESPONSES:
    emoji, message = MOOD_RESPONSES[user_mood]
    print(f"{emoji} {message}")
else:
    # Step 5: Default response
    print("🙂 I don't recognize that mood, but I hope you have a great day!")
