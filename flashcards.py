from flashcards_helper import *

cards = read_cards("TeamPlayers.txt")

for prompt, answer in cards.items():
    flashcard(prompt,answer)



