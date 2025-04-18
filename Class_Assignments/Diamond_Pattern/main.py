"""
Write a Python program to draw a diamond of "*" using loops and string repetition.
"""

def diamond_pattern():
    num = 5
    for i in range(1, num+1):
        print(" " * (num - i) + "*" * (2 * i-1))

    for i in range(num-1, 0, -1):
        print(" " * (num - i) + "*" * (2 * i-1))

diamond_pattern