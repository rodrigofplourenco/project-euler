maxNumber = 4000000
fib = [0, 1]

while fib[-1] <= maxNumber:
  fib.append(fib[-1] + fib[-2])

print(sum(x for x in fib if x % 2 == 0 and x <= maxNumber))
