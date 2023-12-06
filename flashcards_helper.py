def read_cards(filename):
    cards = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            parts = line.split(",")
            cards[parts[1]] = parts[0]
    return cards

def flashcard(prompt,expected_answer):
    answer = input("The Team Player"+prompt+ " played for which team"+"?")
    if answer.lower() == expected_answer.lower():
        print("Correct!")
    else:
        print("Sorry, that is wrong....")    




