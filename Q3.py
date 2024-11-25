import string

def is_pangram(sentence: str, alphabet=string.ascii_lowercase) -> bool:
    # Convert the sentence to lowercase and replace spaces (optional if sentence has no punctuation)
    sentence = sentence.lower().replace(" ", "")
    # Convert sentence to a set of characters and check if it includes all letters in the alphabet
    return set(alphabet).issubset(set(sentence))

# Using the provided sentence
print("The quick brown fox jumps over the lazy dog is : ",is_pangram("The quick brown fox jumps over the lazy dog"))  # Should return True
print("Hello World is : ", is_pangram("Hello World"))  # Should return False
