import time
import random


def slow_print(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")


def start_game():
    slow_print("Welcome to Love.exe - A Terminal Dating Adventure!")
    player_name = input("What's your name? ")
    slow_print(f"Nice to meet you, {player_name}! Let's find your perfect match.\n")
    main_menu(player_name)


def main_menu(player_name):
    slow_print("Choose your potential date:")
    slow_print("1. Alex - The intellectual bookworm")
    slow_print("2. Jordan - The adventurous thrill-seeker")
    slow_print("3. Sam - The sarcastic realist")

    choice = input("Who do you want to meet? (1/2/3): ")
    if choice == "1":
        date_alex(player_name)
    elif choice == "2":
        date_jordan(player_name)
    elif choice == "3":
        date_sam(player_name)
    else:
        slow_print("Invalid choice. Try again.")
        main_menu(player_name)


def relationship_score_system(score):
    if score >= 5:
        slow_print("[ENDING: True Love Connection]")
    elif score >= 3:
        slow_print("[ENDING: Mutual Interest]")
    elif score >= 1:
        slow_print("[ENDING: Friendzone]")
    else:
        slow_print("[ENDING: Ghosted]")


def date_alex(player_name):
    score = 0
    slow_print("You meet Alex at a cozy café, sipping on a latte and reading a book.")
    slow_print("Alex: Oh, hey! I wasn't expecting company. Do you like reading?")
    slow_print(
        "1. Yes, I love books! What's your favorite?\n2. Not really, I'm more into movies.\n3. Books are boring.")

    choice = input("Your choice: ")
    if choice == "1":
        slow_print("Alex: That's awesome! I love discussing literature. Let's meet again!")
        score += 2
    elif choice == "2":
        slow_print("Alex: Hmm, movies can be great too. Maybe we can find common ground?")
        score += 1
    else:
        slow_print("Alex: Oh... I see. Maybe we're not a good match.")

    random_event()
    relationship_score_system(score)


def date_jordan(player_name):
    score = 0
    slow_print("You meet Jordan at an indoor rock climbing gym, full of energy.")
    slow_print("Jordan: Hey! Ready for some adventure?")
    slow_print(
        "1. Absolutely! I love trying new things!\n2. Umm... maybe something safer?\n3. No way, I hate physical activities.")

    choice = input("Your choice: ")
    if choice == "1":
        slow_print("Jordan: That's the spirit! Let's climb together!")
        score += 2
    elif choice == "2":
        slow_print("Jordan: Hey, no worries! Maybe we can go hiking instead?")
        score += 1
    else:
        slow_print("Jordan: Ah, I see. I think we might be too different.")

    random_event()
    relationship_score_system(score)


def date_sam(player_name):
    score = 0
    slow_print("You meet Sam at a small diner, smirking as they sip coffee.")
    slow_print("Sam: So, tell me, what’s the worst pickup line you've ever heard?")
    slow_print(
        "1. 'Are you a magician? Because whenever I look at you, everyone else disappears.'\n2. 'Did it hurt? When you fell from heaven?'\n3. 'I don’t do pickup lines, they’re lame.'")

    choice = input("Your choice: ")
    if choice == "1":
        slow_print("Sam: Wow, that's bad. I like your sense of humor!")
        score += 2
    elif choice == "2":
        slow_print("Sam: Classic, but overused. Still, I appreciate the effort.")
        score += 1
    else:
        slow_print("Sam: Harsh, but fair. Honesty is good.")

    random_event()
    relationship_score_system(score)


def random_event():
    events = [
        "A waiter spills a drink on your date! How do you react?",
        "Your date’s ex suddenly walks in! What do you do?",
        "A random person mistakes you for a celebrity and interrupts the date!"
    ]
    event = random.choice(events)
    slow_print(f"Random Event: {event}")
    slow_print("1. Stay calm and handle it well.\n2. Panic and make it awkward.\n3. Ignore it completely.")

    choice = input("Your reaction: ")
    if choice == "1":
        slow_print("Your date is impressed by how well you handled that!")
    elif choice == "2":
        slow_print("That was a bit awkward, but recoverable.")
    else:
        slow_print("Your date seems confused by your reaction.")


if __name__ == "__main__":
    start_game()
