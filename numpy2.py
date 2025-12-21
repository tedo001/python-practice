import numpy as np

arr = np.array([
    [['a','b','c'], ['d','e','f'], ['g','h','i']],
    [['j','k','l'], ['m','n','o'], ['p','q','r']],
    [['s','t','u'], ['v','w','x'], ['y','z',' ']]
])

word = ""

n = int(input("How many letters do you want? "))

for i in range(n):
    print(f"Enter indexes for letter {i+1}")
    k = int(input("Layer : "))
    r = int(input("Row : "))
    c = int(input("Column : "))

    word += arr[k][r][c]

print("Word formed:", word)
print("Array shape:", arr.shape)
