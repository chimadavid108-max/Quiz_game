from mytools import line

def save_score(date_and_time, score):
    with open("scores.txt", "a") as file:
        file.write(f"{date_and_time}\nScore: {score}\n{line()}\n")