import os

def read_cards(filename):
    cards = {}
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, filename)
    with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    break
                parts = line.split(",")
                cards[parts[1]] = parts[0]
    return cards

def flashcard(prompt, expected_answer):
    answer = input("The Team Player " + prompt + " played for which team" + "? ")
    if answer.lower() == expected_answer.lower():
        print("Correct!")
        return 1
    else:
        print("Sorry, that is wrong....")    
        return 0

