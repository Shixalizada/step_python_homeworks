from functools import wraps
import time

players = [
    {"name": "Ali", "score": 120},
    {"name": "Nigar", "score": 340},
    {"name": "Kamran", "score": 90},
]


def add_player(players, name, score):
    players.append({"name": name, "score": score})
    return players


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} funksiyası {end - start:.6f} saniyə işlədi.")
        return result

    return wrapper


@timer
def top_players(players, n=3):
    return sorted(players, key=lambda p: p["score"], reverse=True)[:n]


def average_score(players):
    if not players:
        return 0
    return sum(player["score"] for player in players) / len(players)


def shout(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() + "!!!"

    return wrapper


@shout
def greet(name):
    return f"salam, {name}"


def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Start!"


if __name__ == "__main__":
    print("=== DƏRS 2 ===")

    add_player(players, "Leyla", 250)

    print("\nTop oyunçular:")
    print(top_players(players, 3))

    print("\nOrta bal:")
    print(average_score(players))

    print("\nShout decorator:")
    print(greet("ali"))
    print("greet.__name__ =", greet.__name__)

    print("\nCountdown:")
    for item in countdown(3):
        print(item)
