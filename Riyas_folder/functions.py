def find_odd_even(numbers):
    odd = [num for num in numbers if num % 2 != 0]
    even = [num for num in numbers if num % 2 == 0]
    return {'odd': odd, 'even': even}

# Example usage:
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_odd_even(sample_list)
    print("Odd numbers:", result['odd'])
    print("Even numbers:", result['even'])