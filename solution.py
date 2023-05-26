import itertools
import re

whole_stmt = "SEND + MORE = MONEY"
# whole_stmt = "DONALD + GERALD = ROBERT"

########################################################################################################################

stmt_charset = set([c for c in whole_stmt if c.isalpha()])
assert len(stmt_charset) <= 10

left_part_for_eval = whole_stmt[0: whole_stmt.find('=')].replace(' ', '')
right_part_for_eval = whole_stmt[whole_stmt.find('=') + 1:].replace(' ', '')

words = re.split(r"\+|-|=|\*", whole_stmt.replace(' ', ''))
max_word_len = max([len(word) for word in words])

chars_cannot_be_zero = {word[0] for word in words}

print(f"Puzzle to solve: {left_part_for_eval}={right_part_for_eval}")
print(f"Unique chars in puzzle: {stmt_charset}")
print(f"Chars cannot be zero: {chars_cannot_be_zero}")

charset_for_absent_digits = set("!@#$%^&*()"[:10 - len(stmt_charset)])
permutations = itertools.permutations(stmt_charset | charset_for_absent_digits)

count = 0
results = []

# Main cycle
for i in permutations:

    map_ = dict(zip(i, "0123456789"))
    trans_table = str.maketrans(''.join(i), "0123456789")

    if [char for char in chars_cannot_be_zero if map_[char] == '0']:
        continue

    right_str = ''.join([map_[c] for c in right_part_for_eval])
    right_val = eval(right_str)
    left_str = ''.join([map_.get(c, c) for c in left_part_for_eval])
    left_val = eval(left_str)

    if right_val == left_val:
        filtered_solution = {k: v for k, v in map_.items() if k.isalpha()}  # Remove non-used chars
        if filtered_solution in results:
            continue
        count += 1
        results.append(filtered_solution)
        print(f"\nPossible solution: {filtered_solution}")
        print(f"\n"  # Works only for 3-word puzzle 
              f"{words[0].translate(trans_table):>12}\n"
              f"+{words[1].translate(trans_table):>11}\n"
              f"{'-' * (max_word_len + 1):>12}\n"
              f"{words[2].translate(trans_table):>12}\n")

print(f"Total solutions number: {count}")
