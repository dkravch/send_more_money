from itertools import permutations

whole_stmt = "SEND + MORE = MONEY"
print(set([c for c in whole_stmt if c.isalpha()]))

stmt_chars = set([c for c in whole_stmt if c.isalpha()])

left_part = whole_stmt[0: whole_stmt.find('=')].replace(' ', '')
right_part = whole_stmt[whole_stmt.find('=') + 1:].replace(' ', '')

print(f"{left_part}={right_part}")


perm = permutations(stmt_chars | {'A', 'B'})

count = 0

for i in perm:

    map_ = dict(zip(i, "0123456789"))

    if map_['S'] == '0' or map_['M'] == '0':
        continue

    right_str = ''.join([map_[c] for c in right_part])
    right_val = eval(right_str)

    left_str = ''.join([map_.get(c, c) for c in left_part])
    left_val = eval(left_str)

    if right_val == left_val:
        count += 1
        print(map_)
        print(f"\n {left_str[0:4]}\n{left_str[4:]}\n-----\n{right_str}\n")
        print("* * *\n")

print(count)
