def equation_straight_line(first_interval: list, second_interval: list, variable: float):
    """
    Equation of a straight line:
    y = mx + n

    Angular coefficient:
    m = (y2 - y1) / (x2 - x1)

    Linear coefficient:
    n = y1 - m * x1
    n = y2 - m * x2

    Original:
    (y2 - y1) / (x2 - x1) * variable + y1 - (y2 - y1) / (x2 - x1) * x1
    (y2 - y1) / (x2 - x1) * variable + y2 - (y2 - y1) / (x2 - x1) * x2

    Short version:720
    y1 + (y2 - y1) * (variable - x1) / (x2 - x1)
    y2 - (y2 - y1) * (x2 - variable) / (x2 - x1)
    """
    assert len(first_interval) == 2 == len(second_interval), "list must have len 2"
    x1, y1 = first_interval
    x2, y2 = second_interval
    return y1 + (y2 - y1) * (variable - x1) / (x2 - x1)


def x_range(max_range: int, mod: int, variable: int):
    x = variable + mod - 1 - variable % mod
    y = 0 ** (variable % max_range) * (mod - 1)
    return x - y


def prime_list(limit):
    # Initialize list to store prime numbers
    primes = []

    # Initialize a list to mark numbers as prime or non-prime
    is_prime = [True] * (limit + 1)

    # Mark 0 and 1 as non-prime
    is_prime[0] = is_prime[1] = False

    # Iterate over the range from 2 to the limit
    for i in range(2, limit + 1):
        # If the number is marked as prime
        if is_prime[i]:
            # Add it to the list of primes
            primes.append(i)

            # Mark all multiples of the prime as non-prime
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Return the list of primes
    return primes

def happy_number(number: int) -> bool:
    happy = 1
    square = 2
    seen = set()

    while number != happy and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** square for digit in str(number))

    return number == happy

if __name__ == "__main__":
    min = [0, 100]
    max = [100, 250]
    test = equation_straight_line(first_interval=min, second_interval=max, variable=5)
    print(test)
    # pri = prime_list(547)
    # for index, primes in enumerate(pri):
    #     result = (11 * primes + index * 5) ** 2 + primes * 137
    #     print(f"{result:,}", index)