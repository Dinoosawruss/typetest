"""Various utility functions."""


def damerau_levenshtein_distance(word_1: str, word_2: str) -> int:
    """Calculates the distance between two words."""
    inf = len(word_1) + len(word_2)
    table = [
        [inf for _ in range(len(word_1) + 2)] for _ in range(len(word_2) + 2)
    ]

    for i in range(1, len(word_1) + 2):
        table[1][i] = i - 1
    for i in range(1, len(word_2) + 2):
        table[i][1] = i - 1

    last_encountered_cols = {}
    for col, char_1 in enumerate(word_1, 2):
        last_row = 0
        for row, char_2 in enumerate(word_2, 2):
            last_encountered_col = last_encountered_cols.get(char_2, 0)

            addition = table[row - 1][col] + 1
            deletion = table[row][col - 1] + 1
            substitution = table[row - 1][col - 1] + (
                0 if char_1 == char_2 else 1
            )

            transposition = (
                table[last_row - 1][last_encountered_col - 1]
                + (col - last_encountered_col - 1)
                + (row - last_row - 1)
                + 1
            )

            table[row][col] = min(
                addition, deletion, substitution, transposition
            )

            if char_1 == char_2:
                last_row = row
        last_encountered_cols[char_1] = col

    return table[len(word_2) + 1][len(word_1) + 1]
