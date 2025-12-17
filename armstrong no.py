num = int(input("Enter number: "))
sum = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if num == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")
