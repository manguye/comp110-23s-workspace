"""EX06 - Choose Your Own Adventure."""

__author__ = "730411646"


points: int = 0
player: str = ""

def main() -> None:
    """The beginning."""
    global points
    greet()

def greet() -> None:
    """Welcome message."""
    global player
    print("Context.")
    player = input("What is your name? ")

if __name__ == "__main__":
    main()