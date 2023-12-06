from flashcards_helper import *
import random

cards = read_cards("TeamPlayers.txt")
total_questions = len(cards)
count_right = 0

prompts = list(cards.keys())
random.shuffle(prompts)

for prompt in prompts:
    count_right += flashcard(prompt, cards[prompt])

print(f"You got {count_right} out of {total_questions} correct.")



