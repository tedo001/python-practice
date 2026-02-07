size = int(input("Enter size of array: "))

results = []

for i in range(size):
    value = input(f"Enter value {i+1}: ")
    digit_sum = 0

    for ch in value:
        digit_sum += int(ch)

    results.append(digit_sum + 1)

for res in results:
    print(res)
