import re
from tkinter import *
import string
COMMON_PASSWORDS = {
    "123456", "123456789", "12345678", "12345", "1234567", "1234567890",
    "password", "password1", "password123", "passw0rd", "p@ssw0rd",
    "qwerty", "qwerty123", "qwertyuiop", "abc123", "111111", "000000",
    "iloveyou", "admin", "admin123", "welcome", "login", "letmein",
    "monkey", "dragon", "football", "baseball", "sunshine", "princess",
    "master", "hello","Password1!", "freedom", "whatever", "trustno1", "1q2w3e4r",
    "654321", "666666", "121212", "123123", "112233", "123321", "987654321",
    "1234", "12345678910", "11111111", "00000000", "123456a", "a123456",
    "1q2w3e", "1qaz2wsx", "qazwsx", "zxcvbnm", "asdfgh", "asdfghjkl",
    "qwerty1", "qwerty12", "qwe123", "q1w2e3r4", "zaq12wsx",

    # common words
    "letmein1", "welcome1", "welcome123", "admin1234", "root", "toor",
    "default", "guest", "test", "test123", "user", "secret", "changeme",
    "pass", "pass123", "pass1234", "passw0rd1", "password!", "password12",
    "password1234", "iloveyou1", "login123", "master123", "access",

    # names, hobbies, popular things
    "superman", "batman", "starwars", "hello123!", "pokemon", "naruto", "minecraft",
    "michael", "jessica", "ashley", "daniel", "charlie", "jordan", "hunter",
    "soccer", "hockey", "cricket", "shadow", "ninja", "killer", "cookie",
    "summer", "winter", "flower", "lovely", "angel", "tigger", "buster",
    "mustang", "harley", "ranger", "matrix", "computer", "internet",

    # love and phrases
    "iloveu", "loveyou", "babygirl", "lovers", "forever", "blink182",
    "letmein123", "monkey123", "dragon123", "sunshine1", "princess1",
}


def show_page(page):
    page.tkraise()


def check_password_strength(password):
    result_list.delete(0, END)
    score = 0
    feedback = []
    force_week = False
    lowered = password.lower()
    stripped = lowered.rstrip(string.digits + string.punctuation)
    
    if lowered in COMMON_PASSWORDS or stripped in COMMON_PASSWORDS:
        feedback.append(f"'{password}' is too common and easy to guess.\n Try and Use another password")
    else:
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password is too short (min 8 characters).")

        if re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Add lowercase letters.")

        if re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("Add uppercase letters.")

        if re.search(r"[0-9]", password):
            score += 1
        else:
            feedback.append("Add numbers.")

        if re.search(r"[^A-Za-z0-9]", password):
            score += 1
        else:
            feedback.append("Add special characters.")
        if len(set(password)) <=3:
            feedback.append("Use more different characters")
            force_week = True 
    if force_week or score <= 3:
        strength = "Weak"
    elif score < 5:
        strength = "Good"
    else:
        strength = "Strong"

    strength_label.config(text=f"Your password strength is {strength}")

    if not feedback:
        feedback.append("Great! No issues found.")

    for i, item in enumerate(feedback, start=1):
        result_list.insert(END, f"{i}. {item}")


def submit():
    # Read the password BEFORE clearing the entry box
    password = entry.get()
    entry.delete(0, END)
    show_page(check_page)
    check_password_strength(password)


def go_home():
    entry.delete(0, END)
    show_page(home_page)


# ---------- Window ----------
root = Tk()
root.title("Password Checker")
root.geometry("500x420")

box = Frame(root)
box.pack(fill="both", expand=True)
box.grid_rowconfigure(0, weight=1)
box.grid_columnconfigure(0, weight=1)

home_page = Frame(box)
check_page = Frame(box)

for p in (home_page, check_page):
    p.grid(row=0, column=0, sticky="nsew")

# ---------- Home page ----------
Label(home_page, text="Password Strength Analysis",
         font=("Arial", 18, "bold")).pack(padx=10, pady=10)
Label(home_page, text="Enter your password:").pack()

entry = Entry(home_page, width=40, show="*")
entry.pack(padx=10, pady=10)
entry.bind("<Return>", lambda event: submit())

Button(home_page, text="Submit", width=10, height=2,
          command=submit).pack(padx=10, pady=10)

# ---------- Result page ----------
strength_label = Label(check_page, text="", font=("Arial", 18, "bold"))
strength_label.pack(padx=10, pady=10)

result_list = Listbox(check_page, width=60, height=8,
                         font=("Segoe UI", 10, "bold"))
result_list.pack(pady=5)

Button(check_page, text="Go to home page", width=20, height=2,
          command=go_home).pack(padx=10, pady=10)

show_page(home_page)
root.mainloop()