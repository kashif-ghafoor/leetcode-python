heights = [5, 1, 2, 3, 4]
ordered = sorted(heights)

notMatch = 0
for unord, ord in zip(heights, ordered):
    if (unord != ord):
        notMatch += 1

print(notMatch)
