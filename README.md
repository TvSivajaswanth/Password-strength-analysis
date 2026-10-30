# Password-strength-analysis
A password strength analysis using Python.

A small desktop app built with Python and Tkinter that rates how strong a password is and tells you exactly what to improve. Type a password, press Submit (or Enter), and get a rating of **Weak**, **Good**, or **Strong** with a numbered list of suggestions.

## Features

- Rates a password as Weak, Good, or Strong
- Gives a numbered list of specific suggestions, such as "Add numbers" or "Password is too short"
- Detects common passwords from a built-in list of well-known weak passwords
- Catches simple variations of common passwords. For example, `Password1!` and `Hello456!` are flagged, because removing the digits and symbols at the end leaves a common word
- Spots passwords made of too few different characters, like `aaaaaaaaaaaa`
- Hides the password while you type (shown as `*`)
- Press **Enter** to submit
- The password box is cleared after checking, and nothing is saved to a file

## How the rating works

Points are added for each rule the password passes:

| Rule | Points |
|---|---|
| 12 or more characters | 2 |
| 8 to 11 characters | 1 |
| Has a lowercase letter | 1 |
| Has an uppercase letter | 1 |
| Has a number | 1 |
| Has a special character | 1 |

The total score is turned into Weak, Good, or Strong.

Some problems force a **Weak** rating, no matter how high the score is:

- The password is in the common-password list, or becomes a common password once trailing digits and symbols are removed
- The password is shorter than 8 characters
- The password uses 3 or fewer different characters

This matters because a password like `Password1!` passes every normal rule, but it is one of the easiest passwords to guess.

## Tech stack

- Python 3
- Tkinter (included with Python)
- `re` (regular expressions) and `string` from the standard library

There are no extra packages to install.

## How to run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## Project structure

```
password-strength-analysis/
├── main.py            # the whole application
└── README.md
```

## How it works

- **Pages:** the app has two `Frame` pages (home and result) stacked in the same grid cell. `show_page()` brings one to the front with `tkraise()`.
- **Regular expressions:** `re.search` checks whether the password contains lowercase letters, uppercase letters, digits, or special characters.
- **Common-password check:** the password is lowercased, then digits and symbols are removed from the end with `rstrip(string.digits + string.punctuation)`. Both versions are checked against a set of common passwords, which is fast because a set looks things up instantly.
- **No widget pile-up:** the result list and labels are created once, and each check only updates them. The list is cleared with `delete(0, END)` before new suggestions are added.

## Privacy

The password is only used to calculate the rating. It is not saved, logged, or sent anywhere.

## Limitations

This is a learning project, not a security tool:

- The common-password list is small, with about a hundred entries. Real tools check millions of leaked passwords.
- It checks rules, not how long a password would actually take to guess. A password can pass every rule here and still be weak.
- For real use, look at estimator libraries such as `zxcvbn`, and use a password manager.

## What I learned

- Building a multi-page Tkinter app
- Using regular expressions for simple pattern checks
- Working with sets, lists, and string methods like `lower()` and `rstrip()`
- Keeping checking logic separate from the interface
- Avoiding the "new widget on every click" bug by creating widgets once and updating them
- Reading error messages and tracing code by hand to find bugs

## A note on how this was built

I built this project while learning, with help from AI. I tested it with different passwords, traced the logic by hand, and fixed bugs along the way, including a crash caused by a wrongly written comparison and a bug where widgets piled up on every click.

## Future improvements

- [ ] Load a much larger common-password list from a file
- [ ] Add a "Show password" checkbox
- [ ] Show a colored strength bar
- [ ] Add a random password generator
- [ ] Check for keyboard patterns such as `qwerty` or `1234`
- [ ] Add a version that runs in the terminal

## License

This project is open source and free to use for learning.
