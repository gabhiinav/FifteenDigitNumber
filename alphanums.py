from random import choice
from collections import Counter
from math import factorial
import string

def generate_and_analyze_alphanumeric():
    chars = string.digits + string.ascii_uppercase
    
    random_string = ''.join(choice(chars) for _ in range(15))
    
    numbers_only = ''.join(char for char in random_string if char.isdigit())
    number_count = Counter(numbers_only)
    
    total_numbers = len(numbers_only)
    denominator = 1
    for count in number_count.values():
        denominator *= factorial(count)
    
    unique_permutations = 0
    if total_numbers > 0:
        unique_permutations = factorial(total_numbers) // denominator
    
    return {
        'string': random_string,
        'total_numbers': total_numbers,
        'number_frequencies': dict(number_count),
        'unique_number_permutations': unique_permutations
    }

result = generate_and_analyze_alphanumeric()

print(f"Generated string: {result['string']}")
print(f"Numbers found: {result['total_numbers']}")
print("\nNumber frequencies:")
for digit, freq in sorted(result['number_frequencies'].items()):
    print(f"{digit}: {freq}")
print(f"\nTotal unique permutations of numbers: {result['unique_number_permutations']}")