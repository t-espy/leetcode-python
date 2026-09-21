def length_of_longest_substring(s: str) -> int:
    last_index: dict[str, int] = {}
    start = 0
    best = 0
    for index, char in enumerate(s):
        seen = last_index.get(char)
        if seen is not None and seen >= start:
            start = seen + 1
        last_index[char] = index
        length = index - start + 1
        if length > best:
            best = length
    return best
