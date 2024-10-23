num = int(input("ENTER A NUMBER: "))
sum_of_factors = 0
for i in range(1, num):
    if num % i == 0:
            sum_of_factors += i

if sum_of_factors == num:
        print(num,"IS A PERFECT NUMBER.")
else:
        print(num,"IS NOT A PERFECT NUMBER.")