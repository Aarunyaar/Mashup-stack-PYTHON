start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end + 1):
    sum = 0
    temp = num
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if num == sum:
        print(num)
