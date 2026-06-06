import os
import datetime
from questions import get_questions as gq
from score import save_score as ss

#---------------------------------------------
# UI HELPERS
#---------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    return "-" * 42

def title(text):
    print(line())
    print(text.center(40))
    print(line())

#---------------------------------------------
# MAIN PROGRAM
#---------------------------------------------
def quiz_app():
    while True:
        clear_screen()
        title("MATHS QUIZ GAME")

        print("""
1. Start New Game
2. View Scores
3. Clear Scores
4. How to Play
5. Exit
""")

        op = input("Select option: ").strip()

#---------------------------------------------
# START GAME
#---------------------------------------------
        if op == "1":
            clear_screen()
            title("NEW GAME")

            score = 0

            # Difficulty input
            while True:
                difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
                if difficulty in ["easy", "medium", "hard"]:
                    break
                print("❌ Invalid difficulty!\n")

            qs = gq(difficulty)

            clear_screen()
            title(f"{difficulty.upper()} MODE")

#---------------------------------------------
            # Game loop
            for key, value in qs.items():
                print(f"\nQ{key}: {value['question']}")

                ans = input("Your answer: ").strip()

                try:
                    if float(ans) == float(value['answer']):
                        print("✅ Correct\n")
                        score += 10
                    else:
                        print(f"❌ Wrong! Answer: {value['answer']}\n")
                except ValueError:
                    print("❌ Invalid input! Counted as wrong.\n")

#---------------------------------------------
            # Save score
            now = datetime.datetime.now().strftime("%d %B %Y")
            ss(now, f"{score}")

            print(line())
            print(f"🎯 FINAL SCORE: {score}")
            print(line())

            input("\nPress Enter to continue...")

#---------------------------------------------
# VIEW SCORES
#---------------------------------------------
        elif op == "2":
            clear_screen()
            title("SCORE HISTORY")

            try:
                with open("scores.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("No scores found yet.")

            input("\nPress Enter to continue...")

#---------------------------------------------
# CLEAR SCORES
#---------------------------------------------
        elif op == "3":
            confirm = input("Clear all scores? (yes/no): ").lower()

            if confirm in ["yes", "y"]:
                with open("scores.txt", "w") as file:
                    file.write("")
                print("✅ Scores cleared!")

            input("\nPress Enter to continue...")

#---------------------------------------------
# HOW TO PLAY
#---------------------------------------------
        elif op == "4":
            clear_screen()
            title("HOW TO PLAY")

            print("""
- Choose a difficulty
- Answer math questions
- Each correct answer = +10 points
- Try to get the highest score!
""")

            input("\nPress Enter to continue...")

#---------------------------------------------
# EXIT
#---------------------------------------------
        elif op == "5":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid option")
            input("Press Enter...")

if __name__ == "__main__":
    quiz_app()