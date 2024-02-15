
from numpy import random

def build_board(size):
    board = random.choice(['Empty', 'Red', 'Black'], size=(size, size))
    return board

def get_count(board, item):
    count = (board == item).sum()
    return count

if __name__ == "__main__":
    print("This file is not intended to be run as a main.")
