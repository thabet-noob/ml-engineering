from collections import Counter


def most_frequent(s):
    count = Counter(s)
    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char
    return best


print(most_frequent("Tthabet"))
