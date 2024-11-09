from dataclasses import dataclass
from typing import List, Optional
from config.constants import ENCODED_UTF_8_
from hashlib import sha256
from algorithms.formulas import happy_number


def hash_number(number: int) -> str:
    number_string = str(number).encode(ENCODED_UTF_8_)
    return sha256(number_string).hexdigest().upper()


@dataclass(slots=True)
class CreatePrime:
    prime: int
    happy: bool
    prime_index: Optional[int]
    hash_256: str

    def __post_init__(self):
        self.happy = happy_number(self.prime)
        self.hash_256 = hash_number(self.prime)


@dataclass(slots=True)
class CreateProduct:
    product: int
    primes: List[int]
    cspp: Optional[bool] # chained super prime products
    happy: bool
    prime_index: Optional[int]
    hash_256: str

    def __post_init__(self):
        self.happy = happy_number(self.product)
        self.hash_256 = hash_number(self.product)

@dataclass(slots=True)
class CreateNoPrimeRelated:
    number: int
    primes: List[int]
    happy: bool
    prime_index: Optional[int]
    hash_256: str

    def __post_init__(self):
        self.happy = happy_number(self.number)
        self.hash_256 = hash_number(self.number)

#     def set_odd(self):
#         self.odd = self.number % 2 != 0
#
#     def set_palindrome(self):
#         number_string = str(self.number)
#         self.palindrome = number_string == number_string[::LAST_ELEMENT_]

