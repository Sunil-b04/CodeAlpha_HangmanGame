
# ============================================
#   HANGMAN GAME — CodeAlpha Python Internship
#   Author: CodeAlpha Intern
# ============================================

import random
import os

# ── Word bank with hints ──────────────────────────────────────────
WORD_BANK = [
    ("python",      "A popular programming language 🐍"),
    ("keyboard",    "You type on this 💻"),
    ("algorithm",   "Step-by-step problem-solving method 🔢"),
    ("function",    "A reusable block of code 📦"),
    ("variable",    "Stores a value in memory 🗃️"),
    ("internet",    "Global network of computers 🌐"),
    ("database",    "Organized collection of data 🗄️"),
    ("compiler",    "Translates code to machine language ⚙️"),
    ("terminal",    "Command-line interface 🖥️"),
    ("debugging",   "Finding and fixing errors in code 🐛"),
]

# ── ASCII art stages (0 = fresh, 6 = dead) ───────────────────────
STAGES = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display(word, guessed, wrong, hint):
    clear()
    print("\n" + "="*45)
    print("        🎮  H A N G M A N  🎮")
    print("="*45)
    print(STAGES[wrong])
    print(f"\n  Hint : {hint}")
    shown = "  Word : " + "  ".join(
        ch if ch in guessed else "_ " for ch in word
    )
    print(shown)
    print(f"\n  Wrong guesses : {6 - wrong} left")
    print(f"  Letters used  : {' '.join(sorted(guessed)) or '-'}")
    print("="*45)

def play():
    word, hint = random.choice(WORD_BANK)
    guessed   = set()
    wrong     = 0
    MAX_WRONG = 6

    while wrong < MAX_WRONG:
        display(word, guessed, wrong, hint)

        if all(ch in guessed for ch in word):
            print(f"\n  🎉 YOU WIN!  The word was: '{word.upper()}'")
            return True

        letter = input("\n  Guess a letter: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            input("  ⚠️  Enter exactly ONE letter. (Press Enter)")
            continue
        if letter in guessed:
            input(f"  ⚠️  '{letter}' already guessed! (Press Enter)")
            continue

        guessed.add(letter)

        if letter in word:
            print(f"  ✅  '{letter}' is in the word!")
        else:
            wrong += 1
            print(f"  ❌  '{letter}' is NOT in the word!")

    display(word, guessed, wrong, hint)
    print(f"\n  💀  GAME OVER!  The word was: '{word.upper()}'")
    return False

def main():
    wins = losses = 0
    while True:
        result = play()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\n  📊  Score → Wins: {wins}  |  Losses: {losses}")
        again = input("\n  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print(f"\n  👋  Thanks for playing! Final → W:{wins} L:{losses}\n")
            break

if __name__ == "__main__":
    main()
