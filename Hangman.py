import random
name = ["Shailesh", "Rahul", "Umang", "Kuldeep", "Bhargav", "Jatin", "Hardik", "Hariom", "Mehul", "Rohit"]
word = random.choice(name)
guesses = 10
guessed = []
hidden = ["_"] * len(word)
game_over = False
def update_hidden(guess):
  global hidden
  global word
  for i in range(len(word)):
    if word[i] == guess:
      hidden[i] = guess
def display():
  global hidden
  global guesses
  print(" ".join(hidden))
  print(f"You have {guesses} guesses left.")
print("Welcome to Hangman!")
display()
while not game_over:
  guess = input("Guess a letter: ").lower()
  if len(guess) != 1 or not guess.isalpha():
    print("Invalid input. Please enter a single letter.")
    continue
  if guess in guessed:
    print("You have already guessed that letter. Try again.")
    continue
  guessed.append(guess)
  if guess in word:
    print("Good guess!")
    update_hidden(guess)
    display()
    if "_" not in hidden:
      print("Congratulations! You have guessed the word!")
      game_over = True
  else:
    print("Sorry, that letter is not in the word.")
    guesses -= 1
    display()
    if guesses == 0:
      print(f"Game over. The word was {word}.")
      game_over = True
