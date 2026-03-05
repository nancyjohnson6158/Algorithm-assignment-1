import math

print("Master Theorem Solver")
print("Recurrence form: T(n) = aT(n/b) + f(n)")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
k = int(input("Enter power of n in f(n) (example: n^k): "))

log_val = math.log(a, b)

result = ""

if k < log_val:
    case = "Case 1"
    complexity = f"Theta(n^{round(log_val,2)})"

elif k == log_val:
    case = "Case 2"
    complexity = f"Theta(n^{k} log n)"

else:
    case = "Case 3"
    complexity = f"Theta(n^{k})"

result += f"a = {a}\n"
result += f"b = {b}\n"
result += f"f(n) = n^{k}\n"
result += f"log_b(a) = {round(log_val,2)}\n"
result += f"Master theorem case: {case}\n"
result += f"Final Time Complexity: {complexity}\n"

print("\n", result)

with open("master_theorem_output.txt", "w") as file:
    file.write(result)
