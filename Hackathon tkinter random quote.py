import tkinter as tk 
import random

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Your limitation—it’s only your imagination.",
    "Work hard in silence. Let success make the noise.",
    "Faith can move mountains. – ",
    "God gives his hardest battles to his strongest soldiers.",
    "The best view comes after the hardest climb.",
    "You were born to win, but to be a winner, you must plan to win, prepare to win, and expect to win. – Zig Ziglar",

    "Don’t watch the clock; do what it does. Keep going.” — Sam Levenson",

"Success is not in what you have, but who you are.” — Bo Bennett",

"The harder you work for something, the greater you’ll feel when you achieve it.",

"Dream bigger. Do bigger.",

"Don’t stop when you’re tired. Stop when you’re done.",

"Push yourself, because no one else is going to do it for you.",

",Great things never come from comfort zones.",

"Success doesn’t just find you. You have to go out and get it.",

"Your limitation—it’s only your imagination.",

"Work hard in silence. Let success make the noise.",

"Faith can move mountains.” — Matthew 17:20",

"God gives his hardest battles to his strongest soldiers.",

"The best view comes after the hardest climb.",

"You were born to win, but to be a winner, you must plan to win, prepare to win, and expect to win.” — Zig Ziglar",

",Hardships often prepare ordinary people for an extraordinary destiny.” — C.S. Lewis",

"Don’t wait for opportunity. Create it.",

"Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",

"The key to success is to focus on goals, not obstacles.",

"Dream it. Wish it. Do it.",

"Success doesn’t come from what you do occasionally, it comes from what you do consistently.",

"The only way to do great work is to love what you do.” — Steve Jobs",

"Opportunities don’t happen, you create them.” — Chris Grosser",

"Do what you can with all you have, wherever you are.” — Theodore Roosevelt",

"You are never too old to set another goal or to dream a new dream.” — C.S. Lewis",

"If you can dream it, you can do it.” — Walt Disney",

"It does not matter how slowly you go as long as you do not stop ,",

"Everything you can imagine is real.” — Pablo Picasso",

"What lies behind us and what lies before us are tiny matters compared to what lies within us.” — Ralph Waldo Emerson",

"The best way to predict the future is to create it.” — Abraham Lincoln",

"You miss 100% of the shots you don’t take.” — Wayne Gretzky",

"I find that the harder I work, the more luck I seem to have.” — Thomas ",

"Success is not final, failure is not fatal: It is the courage to continue that counts.” — Winston Churchill",

"It always seems impossible until it’s done.” — Nelson Mandela",

"The only limit to our realization of tomorrow is our doubts of today.” — Franklin D. Roosevelt",

"You don’t have to be great to start, but you have to start to be great.” — Zig Ziglar",

"Everything you’ve ever wanted is on the other side of fear.” — George Addair",

"Success is walking from failure to failure with no loss of enthusiasm.” — Winston Churchill",

"Your time is limited, so don’t waste it living someone else’s life.” — Steve Jobs",

"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.” — Christian D. Larson",

"Motivation is what gets you started. Habit is what keeps you going.” — Jim Ryun",

"Do not wait to strike till the iron is hot; but make it hot by striking.” — William Butler Yeats",

"The secret of getting ahead is getting started.” — Mark Twain",

"It always seems impossible until it’s done.” — Nelson Mandela",

"Don’t limit your challenges. Challenge your limits.",

"Small daily improvements over time lead to stunning results.” — Robin Sharma",

"Your limitation—it's only your imagination.",

"Push yourself because no one else is going to do it for you.",

"Sometimes later becomes never. Do it now.",

"Great things never come from comfort zones.",

"Dream it. Wish it. Do it.",

"Do something today that your future self will thank you for.",

"Little by little, a little becomes a lot.” — Tanzanian Proverb",

"Don’t stop when you’re tired. Stop when you are done.",

"Action is the foundational key to all success.” — Pablo Picasso",

"The harder the battle, the sweeter the victory.",

"Believe in your infinite potential. Your only limitations are those you set upon yourself.",

"Work hard in silence, let success be your noise.",

"Opportunities don’t happen, you create them",

]

# Function to display a random quote
def new_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# Tkinter window setup
root = tk.Tk()
root.title("Random Motivational Quote Generator")
root.geometry("700x400")
root.config(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="✨ Motivational Quote Generator ✨", font=("Arial", 18, "bold"), bg="#f0f8ff")
title_label.pack(pady=20)

# Quote display label
quote_label = tk.Label(root, text="", wraplength=650, font=("Georgia", 14), bg="#f0f8ff", fg="#333", justify="center")
quote_label.pack(pady=30)

# Button to get a new quote
btn = tk.Button(root, text="Show New Quote", command=new_quote, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=15, pady=5)
btn.pack()

# Show the first quote automatically
new_quote()

root.mainloop()
