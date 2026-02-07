size = int(input())

results = []

for i in range(size):
    value = input()
    digit_sum = 0

    for ch in value:
        digit_sum += int(ch)

    results.append(digit_sum + 1)

for res in results:
    print(res)
