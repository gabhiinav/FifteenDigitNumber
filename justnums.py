from random import randint
from collections import Counter
from math import factorial

def generate_and_analyze_number():
    number = ''.join(str(randint(0, 9)) for _ in range(15))
    
    digit_count = Counter(number)
    
    # Multinomial Formula: n! / (n1! * n2! * ... * nk!)
    total_digits = len(number)
    denominator = 1
    for count in digit_count.values():
        denominator *= factorial(count)
    
    unique_permutations = factorial(total_digits) // denominator
    
    return {
        'number': number,
        'digit_frequencies': dict(digit_count),
        'unique_permutations': unique_permutations
    }

result = generate_and_analyze_number()

print(f"Generated number: {result['number']}")
print("\nDigit frequencies:")
for digit, freq in result['digit_frequencies'].items():
    print(f"{digit}: {freq}")
print(f"\nTotal unique permutations: {result['unique_permutations']}")