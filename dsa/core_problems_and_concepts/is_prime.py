from math import floor, sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
            break
    return True


if __name__ == "__main__":
    print(is_prime(20003))
