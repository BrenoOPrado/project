def merge(left, right):
    letters = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            letters.append(left[left_idx])
            left_idx += 1
        else:
            letters.append(right[right_idx])
            right_idx += 1

    letters += left[left_idx:]
    letters += right[right_idx:]

    res = ''
    for letter in letters:
        res += letter

    return res


def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = merge_sort(string[:mid])
    right = merge_sort(string[mid:])

    return merge(left, right)


def is_anagram(first_string, second_string):
    strings = [first_string.lower(), second_string.lower()]

    if first_string == '' and second_string == '':
        return ('', '', False)

    for idx, string in enumerate(strings):
        strings[idx] = merge_sort(string)

    res = (strings[0], strings[1], strings[0] == strings[1])

    return res
