import random

TEMPLATE_WORD_LIST = ["chimp", "quack", "hello", "trees", "apple", "grace"]

def select_secret_word(words=TEMPLATE_WORD_LIST):
    return random.choice(words)

def make_blanks(word):
    return ["_" for _ in word]

def reveal_letters(secret, blanks, guess):
    revealed = 0
    for i, ch in enumerate(secret):
        if ch == guess and blanks[i] == "_":
            blanks[i] = ch
            revealed += 1
    return revealed

def display_blanks(blanks):
    print(" ".join(blanks))

