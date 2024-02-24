from utils import *
import time

def play_game():
    score = 0
    lives = 3
    start_time = time.time()
    countries = shuffle_countries()

    for country in countries:
        capital = country_capitals[country]
        print(f"What is the capital of {country}?")

        lives_remaining = 0
        while lives_remaining < 3:
            user_input = input("Enter your guess: ")
            if get_user_input(user_input, country, capital):
                score += 1
                break
            else:
                lives_remaining += 1
                lives -= 1
                print(f"Try again! You have {lives} lives left.")
        
        if lives_remaining == 3:
            lives = 0
            print("You lost")
            break

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    show_score(score)
    if lives == 0:
        update_leaderboard(score, time_taken)
        display_leaderboard()
    return score, time_taken


def update_leaderboard(score, time_taken):
    with open("leaderboard.txt", "a") as file:
        file.write(f"Score: {score}, Time: {time_taken} seconds\n")

def display_leaderboard():
    print("Leaderboard:")
    with open("leaderboard.txt", "r") as file:
        leaderboard = file.readlines()
        for entry in leaderboard:
            print(entry.strip())

def show_score(score):
    print(f"Your score is: {score} \n")

if __name__ == "__main__":
    while True:
        print("\n")
        print("-=" * 30 + "-")
        print("Welcome to the minigame \"Country guesser\"\n")
        print("Rules are simple, you need to guess the country.")
        print("You have 3 lives , by every incorrect answer you lose one.\n")


        score, time_taken = play_game()
        update_leaderboard(score, time_taken)
