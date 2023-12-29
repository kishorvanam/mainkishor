a = int(input())
prime = 0
for i in range(2,a):
    if a % i == 0:
        prime += 1
if prime == 0:
    print(" prime")
else:
    print("not prime")