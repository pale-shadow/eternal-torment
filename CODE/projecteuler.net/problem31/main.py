"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
from dataclasses import dataclass

@dataclass
class Pounds:
    one: float = 0.01
    two: float = 0.02
    five: float = 0.05
    ten: float = 0.1
    twenty: float = 0.2
    fifty: float = 0.5
    pound: float = 1.0
    two_pound: float = 2.0

if __name__ == "__main__":
    target_amt = "2"

    P = Pounds()
    print("Values: ", str(P))

    
