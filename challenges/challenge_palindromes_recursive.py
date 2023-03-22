def is_palindrome_recursive(word, low_index, high_index):
    if word != '':
        if len(word) == 1:
            return True

        if word[low_index] == word[high_index]:
            if high_index - low_index <= 1 or is_palindrome_recursive(
                word,
                low_index + 1,
                high_index - 1
            ):
                return True
    return False
