def return_evens(numbers):
    """Returns a list of even elements from the input list using list comprehension."""
    return [num for num in numbers if num % 2 == 0]

def make_exclamation(sentences):
    """Returns a list of sentences with exclamation marks at the end using list comprehension."""
    return [sentence + "!" for sentence in sentences]

# Example usage:
#if __name__ == "__main__":
#    print(return_evens([0, 1, 3, 5, 7, 8, 9]))  # Output: [0, 8]
#   print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))  # Output: ["Hello!", "I'm doing great!", "Python is fun!"]