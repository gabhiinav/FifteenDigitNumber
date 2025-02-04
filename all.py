from random import choice
from collections import Counter
from math import factorial
import string

def generate_and_analyze_alphanumeric():
    chars = string.digits + string.ascii_uppercase
    
    random_string = ''.join(choice(chars) for _ in range(15))
    
    char_count = Counter(random_string)

    total_chars = len(random_string)
    denominator = 1
    for count in char_count.values():
        denominator *= factorial(count)
    
    unique_permutations = factorial(total_chars) // denominator
    
    return {
        'string': random_string,
        'char_frequencies': dict(char_count),
        'unique_permutations': unique_permutations
    }

result = generate_and_analyze_alphanumeric()

print(f"Generated string: {result['string']}")
print("\nCharacter frequencies:")
for char, freq in result['char_frequencies'].items():
    print(f"{char}: {freq}")
print(f"\nTotal unique permutations: {result['unique_permutations']}")